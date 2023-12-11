def display_intro():
    
    print("\n---Welcome to CyberSuite---")
    print("\nAn all-in-one utility designed to simplify various tasks and enhance productivity.\n"
          "Whether you're looking to generate secure passwords, remove metadata from images, scan ports, \n"
          "scrape information from the web, encrypt sensitive data and much more\n"
          "the Multitool has you covered. With a friendly interface and a diverse set of tools, \n"
          "this project aims to streamline your workflow and provide a seamless experience for users with different needs.\n")
    
def tool_1():
    
      print("\nPassword Generator Tool\n\n"
            "Overview:\n"
            "The Password Generator tool is designed to simplify the process of creating secure and robust passwords.\n"
            "It provides users with options to generate new passwords, save username and password combinations, and exit the tool.\n\n"

            "Options:\n"
            "1. Generate New Password:\n\n"

            "Selecting this option allows you to generate a new password with customized settings.\n"
            "You will be prompted to enter the desired password length.\n"
            "It is recommended to use a length of more than 8 characters for enhanced security.\n"
            "The generated password will include a combination of numbers, characters, and symbols.\n\n"
            
            "2. Save Username and Password:\n\n"

            "Choose this option to save a username and password combination in a text file.\n"
            "Enter the desired username and password when prompted.\n"
            "The information will be stored in a file, making it easily accessible whenever needed.\n\n"
            
            "3. Exit:\n\n"

            "Select this option to exit the Password Generator tool.\n")
      hold=input()

def tool_2():
      print("\nPort Scanner Tool\n\n"
            "Overview:\n"
            "The Port Scanner tool enables users to scan for active IP addresses and open ports within a specified range.\n" 
            "It offers options to scan a specific IP address, a range of ports on a specific IP,\n" 
            "well-known ports on a specific IP, or an entire subnet for active IP addresses.\n\n"

            "Options:\n"
            "1. Scan a Specific IP with a Specific Port:\n\n"

            "Choose this option to scan a specific IP address for the availability of a particular port.\n"
            "Enter the IP address and the port number when prompted.\n"
            "The tool will indicate whether the specified port is open or closed.\n\n"
            
            "2. Scan a Specific IP with a Specific Port Range:\n\n"

            "Select this option to scan a specific IP address for open ports within a specified range.\n"
            "Enter the IP address, start port, and end port when prompted.\n"
            "The tool will display a list of open ports within the provided range.\n\n"
            
            "3. Scan a Specific IP with Well-Known Ports:\n\n"

            "This option allows you to scan a specific IP address for well-known ports (1-1024).\n"
            "Enter the IP address when prompted.\n"
            "The tool will show any open well-known ports on the specified IP.\n\n"
            
            "4. Scan a Subnet for Active IP Addresses:\n\n"

            "Choose this option to scan an entire subnet for active IP addresses with a specific open port.\n"
            "Enter the subnet (e.g., 192.168.1.0/24) and the port number when prompted.\n"
            "The tool will display a list of active IP addresses along with the open ports.\n\n"
            
            "5. Exit:\n\n"

            "Select this option to exit the Port Scanner tool.\n\n"
            
            "Note: \n"
            "Use this tool responsibly and ensure that you have the necessary permissions to scan the specified IP addresses and ports.\n")
      hold=input()

def tool_3():
      print("\nMetadata Removal Tool\n\n"
            "Overview:\n"
            "The Metadata Removal tool is designed to detect the file type and remove metadata from image files.\n"
            "Metadata can include information such as camera settings, date and time, and geolocation.\n" 
            "This tool provides users with the ability to view detected metadata and choose to remove it from supported image file types.\n\n"

            "Options:\n"
            "Detect the file type:\n\n"

            "Upon entering the path to an image file, the tool detects the file type and informs the user if it's an image or an unsupported file type.\n"
            "If the file is an image, the tool displays the available metadata.\n\n"
            
            "Remove Metadata:\n\n"

            "After detecting metadata, the tool provides the option to remove it.\n"
            "Users can choose to remove metadata, enhancing privacy and reducing file size.\n\n"
            
            "Exit:\n\n"

            "Users can exit the Metadata Removal tool after processing one or more images.\n")
      hold=input()

def tool_4():
      print("\nWeb Scraper Tool\n\n"
            "Overview:\n"
            "The Web Scraper tool is designed to extract content from a website based on user-defined HTML tags.\n"
            "Users can specify the HTML tag they want to target ('div', 'p', 'h1', 'ul', 'li', 'ol', 'table', etc.) \n"
            "and save the scraped content to a file. The tool follows the website's robots.txt file to determine if web scraping is allowed.\n\n"

            "Options:\n"
            "Scrape Content from a Website:\n\n"

            "Users can enter the URL of the website they want to scrape.\n"
            "Specify the HTML tag to target (e.g., 'div', 'p', 'h1') when prompted.\n"
            "The tool fetches the content, saves it to a file with appropriate indentation, and avoids duplicate content.\n"
            "Users have the option to continue scraping more content on the same website.\n\n"
            
            "Exit:\n\n"

            "Users can choose to exit the Web Scraper tool.\n\n"
            
            "Note:\n"
            
            "The tool respects the website's robots.txt file to determine if web scraping is allowed\n")
      hold=input()

def tool_5():
      print("\nEncryption/Decryption Tool\n\n"
            "Overview:\n"
            "The Encryption/Decryption Tool is designed to secure and protect files through encryption using a user-defined password.\n"
            "Users can encrypt and decrypt files seamlessly, ensuring the confidentiality of sensitive data. \n"
            "The tool utilizes the Fernet symmetric key encryption algorithm and Scrypt key derivation function for enhanced security.\n\n"

            "Options:\n"
            "Encrypt a File:\n\n"
            
            "Users can choose to encrypt a file that is in the device or by providing the path to the file and a password.\n"
            "The tool generates a secure key derived from the password and encrypts the file content.\n"
            "A salt file will be generated for each encryption in the same directory as the targeted file.\n"
            "That Salt file will be required to decrypt the file so keep it safe"
            "The encrypted file is then saved, ensuring data confidentiality.\n\n"
            
            "Decrypt a File:\n\n"

            "Users can decrypt an encrypted file by providing the path to the file and the password used during encryption.\n"
            "The tool validates the password, decrypts the file content, and saves the decrypted file.\n\n"
            
            "Exit:\n\n"

            "Users can choose to exit the Encryption/Decryption Tool after processing one or more files.\n\n"
            
            "Note:\n"
            "Ensure that you remember the password used for encryption, as it is required for decryption.\n")
      hold=input()

def tool_6():
      print("\nKeylogger Tool\n\n"
            "Overview:\n"
            "The Keylogger Tool is a discreet application designed to record and log keystrokes made by a user on a computer.\n"
            "It operates silently in the background, capturing keypress events without the user's knowledge.\n" 
            "The tool uses the pynput library to monitor and record keyboard input.\n\n"

            "Functionality:\n"
            "Keystroke Logging:\n\n"

            "The tool records every key pressed by the user.\n"
            "Special keys such as Backspace, Enter, Shift, Space, and Caps Lock are identified and logged appropriately.\n\n"
            
            "Logging to File:\n\n"

            "The captured keystrokes are saved to a log file (log.txt) for later analysis.\n"
            "Special keys are represented in a human-readable format in the log file.\n\n"
            
            "Discreet Operation:\n\n"

            "The Keylogger Tool operates discreetly in the background, capturing keystrokes without displaying any user interface.\n"
            "It can be stopped by pressing the 'Escape' key multiple times.\n")
      hold=input()

def tool_7():
      print("String Encoder/Decoder Tool\n\n"
            "Overview:\n"
            "The String Encoder/Decoder Tool provides a friendly interface for encoding and decoding text using the Vigenère cipher encryption method.\n"
            "It supports both Caesar and Vigenère ciphers, allowing users to secure their messages with personalized keys.\n\n"

            "Encryption Methods:\n\n"
            "Caesar Cipher:\n\n"

            "The Caesar cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.\n"
            "Users can choose the shift value for encoding or decoding.\n\n"
            
            "Vigenère Cipher:\n\n"

            "The Vigenère cipher is an extension of the Caesar cipher, using a keyword to determine the shift for each character in the plaintext.\n"
            "Users provide a key that is repeated to match the length of the plaintext.\n\n"
            
            "Usage:\n"
            "Choose Encryption Method:\n\n"

            "Users are prompted to choose between the Caesar and Vigenère ciphers.\n\n"
            
            "Select Action:\n\n"

            "Specify whether to encode or decode the text.\n\n"
            
            "Enter Text:\n\n"

            "Input the text that needs to be encoded or decoded.\n\n"
            
            "Provide Additional Information:\n\n"

            "For the Caesar cipher, enter the shift value.\n"
            "For the Vigenère cipher, enter the key.\n\n"
            
            "View Result:\n"

            "The tool displays the result of the encryption or decryption process.\n")
      hold=input()

def tool_8():
      print("\n\nFile Integrity Check\n\n"
            "Overview:\n"
            "The File Integrity Check will read all the files in the official Github Repo excluding all database strings and check them against your files.\n"
            "If it detects a file has been modified, it will print to the GUI that a specific file was modified, at what date and time, and send the alert to the database. \n\n"

            "How to refresh tool:\n"
            "By simply pressing enter, the entire tool will refresh itself and check the current state of the files.")
      hold=input()

def display_tools():
    while True:
        print("\nTools Available:\n")
        print("1. Tool - Password Generator")
        print("2. Tool - Port scanner")
        print("3. Tool - Metadata remover")
        print("4. Tool - Web scraper")
        print("5. Tool - Encryption/Decryption")
        print("6. Tool - Key Logger")
        print("7. Tool - String encoder/decoder")
        print("8. Tool - File Integrity Check")
        print("0. Exit")
    
        
        choice_2 = input("\nEnter the number of the tool: ")
        if choice_2 == "1":
            tool_1()
        elif choice_2 == "2":
            tool_2()
        elif choice_2 == "3":
            tool_3()    
        elif choice_2 == "4":
            tool_4()
        elif choice_2 == "5":
            tool_5()
        elif choice_2 == "6":
            tool_6() 
        elif choice_2 == "7":
            tool_7()    
        elif choice_2 == "8":
             tool_8()   
        elif choice_2 == "0":
            break         
        else:
            print("\nInvalid choice. Please enter a valid option.")


if __name__ == "__main__":
    
    display_intro()

    while True:
        print("\nOptions:")
        print("1. Display Tools")
        print("2. Exit")

        choice_1 = input("\nEnter the number of your choice: ")

        if choice_1 == "1":
            display_tools()
        elif choice_1 == "2":
            print("\nExiting the Tools documentation.")
            break
        else:
            print("\nInvalid choice. Please enter a valid option.")