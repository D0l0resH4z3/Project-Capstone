import os
import hashlib
import mysql.connector

# Function to establish a connection to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='your_database_host',
            user='your_database_user',
            password='your_database_password',
            database='your_database_name'
        )
        cursor = conn.cursor()

        return conn, cursor

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None

# Function to insert file change information into the database
def insert_alert_to_database(cursor, filename):
    try:
        cursor.execute('INSERT INTO file_changes (filename) VALUES (%s)', (filename,))
        conn.commit()
        print(f"Alert: {filename} has been modified. Alert sent to the database.")
    except mysql.connector.Error as e:
        print(f"Error inserting alert to the database: {e}")

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
                    # File has been modified, send alert to the database
                    insert_alert_to_database(cursor, filename)
            else:
                file_hashes[file_path] = current_hash

if __name__ == "__main__":
    directory_path = "D:\CapstoneGithub\Project-Capstone"
    file_hashes = {}

    # Establish a connection to the database
    conn, cursor = connect_to_database()

    while True:
        check_file_changes(directory_path)

        # Optional: Adjust the sleep time based on your needs
        try:
            input("Press Enter to check for changes again...")
        except KeyboardInterrupt:
            # Close the database connection on KeyboardInterrupt
            if conn:
                conn.close()
            break
