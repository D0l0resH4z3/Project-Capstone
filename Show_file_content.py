
import os
import subprocess

def list_files(directory):
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    return files

def open_in_notepad(file_path):
    
    subprocess.run(['notepad.exe', file_path])

if __name__ == "__main__":
    directory = r""
    try:
        files = list_files(directory)
        if not files:
            print("\nNo files found in the directory.")
        else:
            print("\nFiles in the directory:")
            for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
            while True:
                file_number = input("Enter the number of the file to open in Notepad (0 to exit): ")
                if file_number.isdigit():
                    file_number = int(file_number)
                    if 0 < file_number <= len(files):
                        file_to_open = os.path.join(directory, files[file_number - 1])
                        open_in_notepad(file_to_open)
                    elif file_number == 0:
                        print("\nExiting...")
                        exit()
                    else:
                        print("\nInvalid file number.")
                        continue
                else:
                    print("\nInvalid input.")
                    
    except FileNotFoundError:
        print("\nDirectory not found.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

