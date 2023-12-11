import os
import hashlib
from firebase_admin import credentials, firestore, initialize_app
from datetime import datetime
import requests

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

def calculate_file_hash(content):
    sha256_hash = hashlib.sha256(content.encode())
    return sha256_hash.hexdigest()

def read_local_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except Exception as e:
        print(f"Error reading local file: {e}")
        return None

def check_file_changes(directory, db, repo_url, file_hashes):
    while True:
        changes_detected = False

        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                file_path = os.path.join(directory, filename)
                local_content = read_local_file(file_path)

                if local_content is None:
                    continue  # Unable to read the local file, skip this file

                current_hash = calculate_file_hash(local_content)

                if file_path not in file_hashes:
                    file_hashes[file_path] = current_hash
                    continue

                if file_hashes[file_path] != current_hash:
                    # File has been modified, send alert to the database
                    insert_alert_to_database(db, filename)
                    file_hashes[file_path] = current_hash
                    changes_detected = True

        if not changes_detected:
            print("No changes detected.")

        try:
            input("Press Enter to check for changes again...")

        except KeyboardInterrupt:
            print("Exiting the program.")
            break

if __name__ == "__main__":
    repo_url = "https://github.com/D0l0resH4z3/Project-Capstone/tree/main"
    # Use the directory of the script as the base directory
    directory_path = os.path.dirname(os.path.abspath(__file__))

    # Establish a connection to the Firebase database
    db = connect_to_database()

    # Initialize the file_hashes dictionary
    file_hashes = {}

    try:
        check_file_changes(directory_path, db, repo_url, file_hashes)

    except KeyboardInterrupt:
        print("Exiting the program.")
