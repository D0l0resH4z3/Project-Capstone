import string
import os
import hashlib
import time  # Add this line to import the time module
from hypercli import hypercli
import getpass
import subprocess
from Password_Generator import connect_to_database, generate_password, save_password_to_database, save_password_to_file

# Hardcoded usernames and passwords
user_credentials = {
    "user1": "password1",
    "user2": "password2",
    # Add more usernames and passwords as needed
}

def login():
    print("Login to access the main menu.")
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
    with open("encoderdecoder.py", "r") as file:
        script_contents2 = file.read()

@cli.entry(menu="Main Menu", option="Image Metadata Remover")
def execs3():
    with open("metedata_removal.py", "r") as file:
        script_contents3 = file.read()

@cli.entry(menu="Main Menu", option="Key Logger")
def execs4():
    with open("keylogger.py", "r") as file:
        script_contents4 = file.read()

@cli.entry(menu="Main Menu", option="Port Scanner")
def execs5():
    with open("port_scanner.py", "r") as file:
        script_contents5 = file.read()

@cli.entry(menu="Main Menu", option="Web Scraper")
def execs6():
    with open("Web_scraper.py", "r") as file:
        script_contents6 = file.read()

@cli.entry(menu="Main Menu", option="Anti-Virus Scan | File Integrity Check")
def execs7():
    # Get the script contents from File_Integrity_Anti-Virus.py
    with open("File_Integrity_Anti-Virus.py", "r") as file:
        script_contents7 = file.read()

    # Define required functions
    def calculate_file_hash(file_path):
        sha256_hash = hashlib.sha256()
        with open(file_path, "rb") as file:
            for byte_block in iter(lambda: file.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def check_file_changes(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                file_path = os.path.join(directory, filename)
                current_hash = calculate_file_hash(file_path)
                
                if file_path in file_hashes:
                    if file_hashes[file_path] != current_hash:
                        print(f"Alert: {filename} has been modified!")
                else:
                    file_hashes[file_path] = current_hash

    # Pass required modules and functions to exec
    exec_globals = {
        "__file__": "File_Integrity_Anti-Virus.py",
        "__name__": "__main__",
        "os": os,
        "hashlib": hashlib,
        "calculate_file_hash": calculate_file_hash,
        "check_file_changes": check_file_changes,
        "file_hashes": file_hashes,  # Pass the dictionary to the exec environment
    }

    exec(script_contents7, exec_globals, locals())
    time.sleep(1)  # Add a delay for better visibility of potential alerts

# run the cli
cli.run()
