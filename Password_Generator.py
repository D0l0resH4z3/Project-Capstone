
import string
import secrets
import firebase_admin
from firebase_admin import credentials, firestore

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
        firebase_admin.initialize_app(cred)
        print("\nDatabase initialized successfully.")
    except Exception as e:
        print(f"\nError initializing Database: {e}")

# Function to generate a strong password of the given length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_chars = [secrets.choice(characters) for _ in range(length)]
    return ''.join(password_chars)

# Function to save a username and password in the database
def save_password_to_database(username, password):
    initialize_firebase()  # Initialize Firebase with hardcoded credentials
    try:
        db = firestore.client()

        # Create a dictionary with credentials and file content
        data_to_save = {'username': username, 'password': password}

        # Add the data to Firestore
        db.collection('credentials').add(data_to_save)
        print("\nPassword saved to the database successfully!")
        hold=input()

    except Exception as e:
        print(f"\nError saving password to the database: {e}")

# Function to save a username and password in a text file
def save_password_to_file(username, password):
    try:
        with open("passwords.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        print("\nPassword saved to the text file successfully!")
        hold=input()

    except IOError as e:
        print(f"\nError saving password to the text file: {e}")
        hold=input()

# Function to get a valid integer input from the user
def get_valid_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.")

if __name__ == "__main__":
    print("\nPassword Manager")

    while True:
        print("\nOptions:")
        print("1. Generate a new password")
        print("2. Save a password to the database")
        print("3. Save a password to a text file")
        print("0. Exit \n")

        choice = input("\nEnter the number of your choice: ")

        if choice == "1":
            password_length = get_valid_integer_input("\nEnter the length of the password: ")
            if password_length < 8:
                print("\nPassword length should be at least 8 characters for security.")
            else:
                password = generate_password(password_length)
                print("\nGenerated Password:", password)
                hold=input()

        elif choice == "2":
            username = input("\nEnter the username: ")
            password = input("Enter the password: ")
            save_password_to_database(username, password)

        elif choice == "3":
            username = input("\nEnter the username: ")
            password = input("Enter the password: ")
            save_password_to_file(username, password)

        elif choice == "0":
            print("\nExiting the Password Manager.")
            break

        else:
            print("\nInvalid choice !!!")
            hold=input()
            