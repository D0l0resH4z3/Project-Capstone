import os
import hashlib
from firebase_admin import credentials, firestore, initialize_app
from datetime import datetime
import keyboard

# Function to initialize Firebase with hardcoded credentials
def initialize_firebase():
    try:
        # Replace the following credentials with your hardcoded values
        cred = credentials.Certificate({
            "type": "",
            "project_id": "",
            "private_key_id": "",
            "private_key": "",
            "client_email": "",
            "client_id": "",
            "auth_uri": "",
            "token_uri": "",
            "auth_provider_x509_cert_url": "",
            "client_x509_cert_url": "",
            "universe_domain": ""
        })
        initialize_app(cred)
        print("\nFirebase initialized successfully.")
    except Exception as e:
        print(f"\nError initializing Firebase: {e}")

# Function to establish a connection to the Firebase database
# Function to establish a connection to the Firebase database
def connect_to_database():
    initialize_firebase()
    try:
        db = firestore.client()
        return db

    except Exception as e:
        print(f"Error connecting to Firebase: {e}")
        return None

# Function to insert file change information into the database with timestamp
def insert_alert_to_database(db, filename):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.collection('file_changes').add({'filename': filename, 'timestamp': timestamp})
        print(f"Alert: {filename} has been modified. Alert sent to the database at {timestamp}")
    except Exception as e:
        print(f"Error inserting alert to the database: {e}")

def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_file_changes(directory, db, file_hashes):
    while True:
        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                file_path = os.path.join(directory, filename)
                current_hash = calculate_file_hash(file_path)

                if file_path not in file_hashes:
                    file_hashes[file_path] = current_hash
                    continue

                with open(file_path, 'r') as file:
                    lines = file.readlines()
                    modified_lines = []

                    for line in lines:
                        if "credentials.Certificate" in line:
                            # Skip the line containing the specific credentials string
                            pass
                        else:
                            modified_lines.append(line)

                    # Update the file if any lines were modified
                    # Comment out the following lines to skip file modification
                    # if modified_lines:
                    #     with open(file_path, 'w') as file:
                    #         file.writelines(modified_lines)

                if file_hashes[file_path] != current_hash:
                    # File has been modified, send alert to the database
                    insert_alert_to_database(db, filename)
                    file_hashes[file_path] = current_hash

        try:
            input("Press Enter to check for changes again...")

        except KeyboardInterrupt:
            print("Exiting the program.")
            break

if __name__ == "__main__":
    directory_path = "D:\\CapstoneGithub\\Project-Capstone"
    
    # Establish a connection to the Firebase database
    db = connect_to_database()

    # Initialize the file_hashes dictionary
    file_hashes = {}

    try:
        check_file_changes(directory_path, db, file_hashes)

    except KeyboardInterrupt:
        print("Exiting the program.")