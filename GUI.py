import string
import os
import hashlib
import time
from hypercli import hypercli
import getpass
import subprocess
import mysql.connector
from Password_Generator import connect_to_database, generate_password, save_password_to_database, save_password_to_file
from File_Integrity_Anti_Virus import connect_to_database, check_file_changes
from encoderdecoder import main as encoderdecoder_main
from metadata_removal import process_image

# Hardcoded usernames and passwords
user_credentials = {
    "user1": "password1",
    "user2": "password2",
    # Add more usernames and passwords as needed
}

def login():
    print("Please enter your login details.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # Check if the entered username and password are valid
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid username or password. Please try again.\n")
        return False

# Add the login prompt before the main menu
while not login():
    pass  # Continue prompting for login until successful

# Establish a connection to the database
conn, cursor = connect_to_database()

# create an instance of hypercli
cli = hypercli()

# configure the instance
cli.config["banner_text"] = "CyberSuite Tools"
cli.config["intro_title"] = "Intro"
cli.config["intro_content"] = "The Ultimate Cyber tools for your needs!"
cli.config["show_menu_table_header"] = True

# Initialize the file_hashes dictionary
file_hashes = {}

# add navigation options to the menu
@cli.entry(menu="Main Menu", option="Password Generator")
def passgenexec():
    # Get password length from user input
    password_length = int(input("\nEnter the length of the password: "))
    if password_length < 8:
        print("\nPassword length should be at least 8 characters for security.")
    else:
        # Generate a password
        password = generate_password(password_length)
        print("\nGenerated Password:", password)

        # Save the password to the database
        save_password_to_database(conn, cursor, "hardcoded_user", password)

        # Save the password to a text file
        save_password_to_file("hardcoded_user", password)

@cli.entry(menu="Main Menu", option="String Encoder/Decoder")
def stringexec():
    method = input("Choose an encryption method (Caesar/Vigenere): ").strip().lower()
    action = input("Enter 'encode' to encode or 'decode' to decode: ").strip().lower()
    text = input("Enter the text: ")

    if method == "caesar":
        shift = int(input("Enter the shift value: "))
        result = encoderdecoder_main(method, action, text, shift=shift)
    elif method == "vigenere":
        key = input("Enter the key: ")
        result = encoderdecoder_main(method, action, text, key=key)

    print(f"Result: {result}")

@cli.entry(menu="Main Menu", option="Image Metadata Remover")
def execs3():
    print("Executing Image Metadata Remover...")
    file_path = input("\nEnter the path to an image: ")
    process_image(file_path)

@cli.entry(menu="Main Menu", option="Key Logger")
def execs4():
    print("Executing Key Logger...")

    # Run keylogger.py as a separate process
    try:
        subprocess.run(["python", "keylogger.py"])
    except KeyboardInterrupt:
        print("Keylogger execution interrupted by user.")
    except Exception as e:
        print(f"Error executing keylogger.py: {e}")

@cli.entry(menu="Main Menu", option="Port Scanner")
def execs5():
    print("Executing Port Scanner...")

    # Run port_scanner.py as a separate process
    try:
        subprocess.run(["python", "port_scanner.py"])
    except KeyboardInterrupt:
        print("Port Scanner execution interrupted by user.")
    except Exception as e:
        print(f"Error executing port_scanner.py: {e}")

@cli.entry(menu="Main Menu", option="Web Scraper")
def execs6():
    print("Executing Web Scraper...")
    
    # Read the script contents directly from the file
    with open("Web_scraper.py", "r") as file:
        script_contents6 = file.read()

    # Save the script contents to a temporary file
    with open("temp_web_scraper.py", "w") as temp_file:
        temp_file.write(script_contents6)

    # Run the temporary script as a separate process
    try:
        subprocess.run(["python", "temp_web_scraper.py"])
    except KeyboardInterrupt:
        print("Web Scraper execution interrupted by user.")
    except Exception as e:
        print(f"Error executing Web Scraper: {e}")

    # Remove the temporary file
    os.remove("temp_web_scraper.py")


@cli.entry(menu="Main Menu", option="Anti-Virus Scan | File Integrity Check")
def execs7():
    # Function to execute File_Integrity_Anti-Virus.py
    def execute_file_integrity_check():
        directory_path = "D:\CapstoneGithub\Project-Capstone"

        # Establish a connection to the database
        conn, cursor = connect_to_database()

        try:
            # Pass conn and cursor to the function
            check_file_changes(directory_path, conn, cursor, file_hashes)

        except KeyboardInterrupt:
            print("Exiting the program.")
            if conn:
                conn.close()

    # Call the function to execute File_Integrity_Anti-Virus.py
    execute_file_integrity_check()
    time.sleep(1)  # Add a delay for better visibility of potential alerts

# run the cli
cli.run()