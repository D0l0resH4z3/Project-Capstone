from PIL import Image
from PIL.ExifTags import TAGS
import os
import time  # Import the time module

def detect_file_type(file_path):
    try:
        _, ext = os.path.splitext(file_path)
        
        if ext.lower() in ('.jpg', '.jpeg', '.png'):
            return 'Image'
        else:
            return 'Unsupported'
        
    except Exception as e:
        print(f"Error detecting file type: {e}")
        return 'Unsupported'

def print_metadata(file_path):
    try:
        image = Image.open(file_path)
        exifdata = image.getexif()

        if not exifdata:
            print("\nNo metadata found.")
            time.sleep(1)  # Add a 1-second delay after printing "No metadata found"
            return None

        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)

            if isinstance(data, bytes):
                data = data.decode()
            print(f"{tag:20}: {data}")

        return True
    except Exception as e:
        print(f"Error reading metadata: {e}")
        return None

def remove_metadata(file_path):
    try:
        image = Image.open(file_path)
        image.save(file_path, exif=b"")
        print("\nMetadata removed.")
        time.sleep(1)  # Add a 1-second delay after successful removal
    except Exception as e:
        print(f"Error removing metadata: {e}")
        time.sleep(1)  # Add a 1-second delay after an error during removal

def process_image(file_path):
    try:
        file_type = detect_file_type(file_path)

        if file_type == 'Unsupported':
            print("\nUnsupported file type.")
        else:
            print(f"\nDetected file type: {file_type}")
            print("\nAvailable Metadata:\n")
            metadata_result = print_metadata(file_path)

            if metadata_result is not None:
                user_choice = input("\nDo you want to remove the metadata? (Y/N): ").lower()
                if user_choice == 'y':
                    remove_metadata(file_path)
    except Exception as e:
        print(f"Error processing image: {e}")
        time.sleep(1)  # Add a 1-second delay after an unexpected error

if __name__ == "__main__":
    while True:
        try:
            file_path = input("\nEnter the path to an image (or 'exit' to quit): ")

            if file_path.lower() == 'exit':
                print("\nExit...\n")
                break

            if not os.path.exists(file_path):
                print("\nError: File not found.")
                continue

            process_image(file_path)
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            time.sleep(1)  # Add a 1-second delay after an unexpected error
