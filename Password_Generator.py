# This program will generate strong passwords with the length of the user`s choice and save passwords with username in a text file
# Import necessary modules
import string
import secrets
import mysql.connector

# Function to establish a connection to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='your_username',
            password='your_password',
            database='your_database'
        )
        cursor = conn.cursor()

        # Create a table to store passwords
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS passwords (
                id INT AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(255),
                password VARCHAR(255)
            )
        ''')
        conn.commit()

        return conn, cursor

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None

# Function to generate a strong password of the given length
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password_chars = [secrets.choice(characters) for _ in range(length)]
    return ''.join(password_chars)

# Function to save a username and password in the database
def save_password_to_database(conn, cursor, username, password):
    try:
        cursor.execute('INSERT INTO passwords (username, password) VALUES (%s, %s)', (username, password))
        conn.commit()
        print("Password saved to the database successfully!")
    except mysql.connector.Error as e:
        print(f"Error saving password to the database: {e}")

# Function to save a username and password in a text file
def save_password_to_file(username, password):
    try:
        with open("passwords.txt", "a") as file:
            file.write(f"Username: {username}, Password: {password}\n")
        print("Password saved to the text file successfully!")
    except IOError as e:
        print(f"Error saving password to the text file: {e}")

if __name__ == "__main__":
    print("\nPassword Manager")

    # Establish a connection to the database
    conn, cursor = connect_to_database()
    
    while True:
        print("\nOptions:")
        print("1. Generate a new password")
        print("2. Save a password to the database")
        print("3. Save a password to a text file")
        print("0. Exit\n")
        
        choice = input("\nEnter the number of your choice: ")
        
        if choice == "1":
            password_length = int(input("\nEnter the length of the password: "))
            if password_length < 8:
                print("\nPassword length should be at least 8 characters for security.")
            else:
                password = generate_password(password_length)
                print("\nGenerated Password:", password)

        elif choice == "2":
            username = input("\nEnter the username: ")
            password = input("Enter the password: ")
            save_password_to_database(conn, cursor, username, password)

        elif choice == "3":
            username = input("\nEnter the username: ")
            password = input("Enter the password: ")
            save_password_to_file(username, password)
        
        elif choice == "0":
            print("\nExiting the Password Manager.")
            if conn:
                conn.close()
            break
        
        else:
            print("Invalid choice !!!")