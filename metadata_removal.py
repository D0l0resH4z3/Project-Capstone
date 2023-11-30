

from PIL import Image
from PIL.ExifTags import TAGS
import os


def detect_file_type(file_path):
    try:
        
        _, ext = os.path.splitext(file_path)
        
        
        if ext.lower() in ('.jpg', '.jpeg', '.png'):
            return 'Image'
        else:
            return 'Unsupported'
        
    except Exception:
        return 'Unsupported'


def print_metadata(image):

    
    exifdata = image.getexif()
    
    if not exifdata:
        
        print("\nNo metadata found.")
        return None
    
   
    for tag_id in exifdata:

        
        tag = TAGS.get(tag_id, tag_id)
        data = exifdata.get(tag_id)

        
        if isinstance(data, bytes):
            data = data.decode()
        print(f"{tag:20}: {data}")

    return True    


def remove_metadata(file_path):
    image = Image.open(file_path)
    image.save(file_path, exif=b"")


if __name__ == "__main__":
    print("\nMetadata remover")
    while True:
        file_path = input("\nEnter the path to an image: ")
        
        if not os.path.exists(file_path):
            print("\nError: File not found.")
            continue 
        
        file_type = detect_file_type(file_path)
        
        if file_type == 'Unsupported':
            print("\nUnsupported file type.")
            
        else:
            print(f"\nDetected file type: {file_type}")
            if file_type == 'Image':
                image = Image.open(file_path)
    
            print("\nAvailable Metadata:\n")
            metadata_result = print_metadata(image)
            
            if metadata_result is not None:
                while True:
                    user_choice = input("\nDo you want to remove the metadata? (Y/N): ").lower()
                    if user_choice == 'y':
                        remove_metadata(file_path)
                        print("\nMetadata removed.")
                        break
                    elif user_choice == 'n':    
                        break
                    else:
                        print("Invalid input !!!")

        while True:        
            another_image = input("\nDo you want to process another image? (Y/N): ").lower()
            if another_image == 'y':
                break
                
            elif another_image == 'n':    
                print("\nExit...\n")
                exit()
            else:
                print("Invalid input !!!")