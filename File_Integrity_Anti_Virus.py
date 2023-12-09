import os
import hashlib
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime

def initialize_firebase(credentials_path):
    try:
        # Initialize Firebase with your credentials
        cred = credentials.Certificate(credentials_path)
        firebase_admin.initialize_app(cred)
        print("Firebase initialized successfully.")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")

def connect_to_firestore():
    db = firestore.client()
    return db

def insert_alert_to_firestore(db, filename):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.collection('file_changes').add({'filename': filename, 'timestamp': timestamp})
        print(f"Alert: {filename} has been modified. Alert sent to Firestore at {timestamp}")
    except Exception as e:
        print(f"Error inserting alert to Firestore: {e}")

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

                if file_path in file_hashes:
                    if file_hashes[file_path] != current_hash:
                        # File has been modified, send alert to Firestore
                        insert_alert_to_firestore(db, filename)
                else:
                    file_hashes[file_path] = current_hash

        try:
            input("Press Enter to check for changes again...")

        except KeyboardInterrupt:
            print("Exiting the program.")
            break

if __name__ == "__main__":
    # Replace 'path to credentials.json' with the actual path to your Firebase credentials JSON file
    credentials_path = r''
    initialize_firebase(credentials_path)

    # Connect to Firestore
    firestore_db = connect_to_firestore()

    directory_path = r""

    # Initialize the file_hashes dictionary
    file_hashes = {}

    try:
        check_file_changes(directory_path, firestore_db, file_hashes)

    except KeyboardInterrupt:
        print("Exiting the program.")
