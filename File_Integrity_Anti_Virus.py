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
        "type": "service_account",
    "project_id": "capstone-usb",
    "private_key_id": "f1ccb9ad4a9c606027c58b6ea58912cf51ee3c58",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDrt078ynO5MA42\nNjcg56a5m7G84/eD+/7iRajeNcT7TsjmgKsfu2Ecco4/TQAxsEafzRM3kAeWEWqp\n7bMmXSc16bInxmUf+5mYqRGVUAbDwYOge/LdHX39neA7iXj6ljpLtUXFpKMnHPNN\n3HDq6hhEhL7ULIf9fGu0Q2b3cARHicbVPrumt4w71DFa2B9pEj2WsVoZaqV4baZZ\n9Wy5zzP3M98cVisb9OrSbJozAns4waulxQd9RnJ9GTE/6XIJ8pcCQG9zwdbKcP8F\n3ERUJYsjVQZK75CFKwj7OPPDQB/K3NpzC9jKJiTlEr7fXOIs/q9Vt2dccfDqLnF3\ndwJQG6W9AgMBAAECggEAMj/Sq9swzlKrRO1L1Uzs4vaI7l6evlkzHeOBu1U1F+nU\ntCbL1Cjq69iT8HSmzPDqLVjXdunSZDB0T6NnpI8JM9oM66PEnQvS05N/NxhnSMXx\nHH4v6OlHmZBVY/vLeYgbB1aueBK/4S+vwnJy8/FRmRG/aJXRq70hbL1NrwQHNYSF\nzSuTOxp5PI14/0iyMlXplI+cnpls/k85aUdCUdusfdN5s0KhqjcQROqRPKIeZ3hm\nRpn1nJGKb+mujp1ugxG93wzs7XaaDDxBJeV2i0Tzvvi9iEqnqtQ0AAYnUP+RWuo5\n9v17s3I5H3Dwws5qoIwN2ppnxA7C0LGoFx0pADaklQKBgQD2yKDNlfjtFkYQnrnb\njvFsf49cHvMestUZ1flqYFEyFN2m5oW7j+jFo1BC9BiQ/KrG3073oi43B4+Wjz9S\nme//KePqfBEUEs1iC0g1j23MB6yiQrJhIi0BhowA4Er/kZB8blaQI6NbIivlykQ9\nXLekRegEF3PShZij+JaPUx3W2wKBgQD0hN5Ge6Z7sJ5tBU7/SMhoFklPt2bEi7nL\nC4fYL0ZMB+ajGNahaJibCtCDwBIdzhiVhn0q6QSSI93icK2xj0QCfiOuBhVLERb4\n1SZ0q9fsL4exLJupptQzBnll5sVeL4VpOn+Lzte56uIBv00020u+u0vtT8HfcVke\nYWhfPy7dRwKBgQCI8D86lTOx66ApbMpZKPKScB4O0iW6LSXO1ks2Wgf0MFvmVxhy\nQaK6uKq63FQdb/cbr6JUCyx14L4un4JVxZHFF2ufHAUmDGDnPLdu8Q3OH5wN1dDB\n0YMDy7M4cT1sn0t7oIZsKTpmQYn2UsyW+DH298uNKa5dbUCMDE8PbOGr7QKBgG6j\nqEfQL1aMZkMCQep1LmkanHV7kP6iEqFzSDZjvbUtZgiqdoN2ZobQ7+SNhiUCWlFe\nF0jRQwY1QHLzdUSAhM9z8AUQL5ZV10UkfVARaZQvNYDPpGexWxbzeP7I2slxSzaA\nB7JlF2vCgh00SGUATVeyO/rXOew2x5JdlPJ0DmqFAoGAW3R6p33WS5DShbuJ+Cl+\no2mYKWtYNq9DTR0wVO6vWCH9riVpyXVA70HSTxrirn6bwtri7jD5YyClMnIT3mbh\n6rREV7mlauYsGgI4o6tXT+sqhYRduVJMPkwJihQyqqRW2AcYVSARfEIywD/DfdD4\naP2pEsn/16frVSH+uud/QFg=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-2i961@capstone-usb.iam.gserviceaccount.com",
    "client_id": "111094319260513196635",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2i961%40capstone-usb.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
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
