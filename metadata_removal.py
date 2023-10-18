# This program will print all the metadata and  remove it from any images selected by the user
# Import necessary modules

from PIL import Image
from PIL.ExifTags import TAGS
import os

# Function to detect the file type 
def detect_metadata_type(file_path):
    try:
        # Split the file path into base name and extension
        _, ext = os.path.splitext(file_path)
        
        # Check if the extension is one of the supported image types
        if ext.lower() in ('.jpg', '.jpeg', '.png'):
            return 'Image'
        else:
            return 'Unsupported'
        
    except Exception:
        return 'Unsupported'

# Function to print the metadata of an image
def print_metadata(metadata):

    # Extract EXIF data from the image
    exifdata = metadata.getexif()
    
    if not exifdata:
        # If no metadata is found, print a message and return None
        print("\nNo metadata found.")
        return None
    
    # Iterating over all EXIF data fields
    for tag_id in exifdata:

        # Get the tag name for humane readable format
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)

        # Decode bytes if necessary
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:20}: {data}")

    return True    

# Function to remove metadata from an image file
def remove_metadata(file_path):
    image = Image.open(file_path)
    image.save(file_path, exif=b"")

# Entry point for the program
if __name__ == "__main__":
    while True:
        file_path = input("\nEnter the path to an image: ")
        metadata_type = detect_metadata_type(file_path)
        if metadata_type == 'Unsupported':
            print("\nUnsupported file type.")
        else:
            print(f"\nDetected file type: {metadata_type}")
            if metadata_type == 'Image':
                image = Image.open(file_path)
                metadata = image
            print("\nAvailable Metadata:\n")
            metadata_result = print_metadata(metadata)
            
            if metadata_result is not None:
                user_choice = input("\nDo you want to remove the metadata? (yes/no): ").strip().lower()
                if user_choice == 'yes':
                    remove_metadata(file_path)
                    print("\nMetadata removed.")
                
        another_image = input("\nDo you want to process another image? (yes/no): ").strip().lower()
        if another_image != 'yes':
            print("\nExit...\n")
            break
