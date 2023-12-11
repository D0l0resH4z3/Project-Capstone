
import subprocess

def update_pip():
    try:
        result = subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'pip'], capture_output=True, text=True, check=True)
        print("\nSuccessfully updated: pip")
    except subprocess.CalledProcessError as e:
        print(f"\nFailed to update pip. Error: {e}")
        print(result.stdout)  
        return result.returncode

def install_library(library):
    try:
        result = subprocess.run(['pip', 'install', library], capture_output=True, text=True, check=True)
        print(f"Successfully installed: {library}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {library}. Error: {e}")
        print(result.stdout)  
        return result.returncode

def install_libraries():
    libraries = ['cryptography','fernet', 'hypercli', 'requests', 
                 'beautifulsoup4', 'pynput', 'Pillow','firebase_admin',
                 'pybase64','pyfiglet ']  

    for library in libraries:
        install_library(library)

if __name__ == "__main__":
    
   
    update_pip()
    
    install_libraries()
