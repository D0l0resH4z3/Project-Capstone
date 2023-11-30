
import cryptography
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt
import secrets
import base64
import os


def derive_key(salt, password):
    
    kdf = Scrypt(salt=salt, length=32, n=2**14, r=8, p=1)
    return kdf.derive(password.encode())

def load_salt(filename):
    
    salt_file_path = filename + ".salt"
    try:
        with open(salt_file_path, "rb") as salt_file:
            return salt_file.read()
    except FileNotFoundError:
        print(f"\nSalt file '{salt_file_path}' not found.")
        return None

def save_salt(filename, salt):

    salt_file_path = filename + ".salt"
    try:
        with open(salt_file_path, "wb") as salt_file:
            salt_file.write(salt)
    except Exception as e:
        print(f"\nError saving salt: {e}")
        
def get_the_filename(directory):
    
    print("\nHere is the list of the files in this device:\n")
    files = [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
    
    for i, file in enumerate(files, start=1):
                print(f"{i}. {file}")
                
    while True:  
        try:
                      
            file_number = int(input("\nEnter the number of the file to encrypt or decrypt \n"
                                    "you can encrypt or decrypt files from different location as well (enter 100): ") )
            
            if 0 < file_number <= len(files):
                return files[file_number - 1]
            
            elif file_number == 100:
                file_path = input("\nEnter the directory path: ")
                return file_path
            else:
                print("\nInvalid input. Please enter a valid number.")
                
              
        except ValueError:
            print("\nInvalid input. Please enter a valid number.")

def generate_key(password, filename, load_existing_salt=False, should_save_salt=True):
    salt_size = 16
   
    if load_existing_salt:
        
        salt = load_salt(filename)
    elif should_save_salt:
        
        salt = secrets.token_bytes(salt_size)
        save_salt(filename, salt)
    
    derived_key = derive_key(salt, password)
    
    return base64.urlsafe_b64encode(derived_key)

def encrypt_file(filename, key):
    
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            
            file_data = file.read()
            
            result_data = f.encrypt(file_data)

        with open(filename, "wb") as file:
            file.write(result_data)

        print("\nFile Encrypted successfully")
        
    except Exception as e:
        print(f"\nError processing file: {e}")
        
def decrypt_file(filename, key):
    
    f = Fernet(key)
    try:
        with open(filename, "rb") as file:
            
            file_data = file.read()
            
            try:
                result_data = f.decrypt(file_data)
                
            except cryptography.fernet.InvalidToken:
                print("\nInvalid password !!!")
                return


        with open(filename, "wb") as file:
            file.write(result_data)

        print("\nFile Decrypted successfully")
        
    except Exception as e:
        print(f"\nError processing file: {e}")

if __name__ == "__main__":
    while True:
        directory_path = r""
        
        file = get_the_filename(directory_path)
        
        while True:
            encrypt_decrypt_input = input("\nDo you want to encrypt or decrypt the file? (E/D): ").lower()
            

            if encrypt_decrypt_input == "e":
                password = input("\nEnter the password for encryption: ")
                key = generate_key(password, file, should_save_salt=True)
                encrypt_file(file, key)
                break
                
            elif encrypt_decrypt_input == "d":
                password = input("\nEnter the password you used for encryption: ")
                key = generate_key(password, file, load_existing_salt=True)
                decrypt_file(file, key)
                break
            
            else:
                print("\nInvalid input !!! Please type 'e' or 'd'")
                
        while True:    
            another_file = input( "\nDo you want to encrypt or decrypt another file? (Y/N): ").lower()
            if another_file == 'yes':
                break
            elif another_file == 'no':    
                    print("\nExit...\n")
                    exit()
            else:
                print("\nInvalid input !!!")