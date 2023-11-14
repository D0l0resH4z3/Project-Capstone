import subprocess


def update_pip():
    try:
        subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'pip'], check=True)
        print("\nSuccessfully updated: pip\n")
    except subprocess.CalledProcessError as e:
        print(f"\nFailed to update pip.\n Error: {e}\n")

def install_libraries(libraries):
    for library in libraries:
        try:
            subprocess.run(['pip', 'install', library], check=True)
            print(f"\nSuccessfully installed: {library}\n")
        except subprocess.CalledProcessError as e:
            print(f"\nFailed to install {library}.\n Error: {e}\n")

def add_user_library(libraries):
    user_input = input("\nDo you want to add any other library (Y/N): \n")
    if user_input.lower() == "y":
        
        user_library = input("\nEnter the name of the library you want to add: \n")
        if user_library:
            
            try:
                subprocess.run(['pip', 'install', user_library], check=True)
                print(f"\nSuccessfully installed: {user_library}\n")
            except subprocess.CalledProcessError as e:
                print(f"\nFailed to install {user_library}.\n Error: {e}\n")
        print("\nDone.\n")        
        
    elif user_input.lower() == "n":
        print("\nDone.\n")
        
        
if __name__ == "__main__":
    libraries_to_install = ['ipaddress', 'cryptography', 'hypercli', 'requests', 'beautifulsoup4', 'bs4', 'pynput', 'os-sys', 'Pillow']
    
    update_pip()
    
    install_libraries(libraries_to_install)
    
    add_user_library(libraries_to_install)