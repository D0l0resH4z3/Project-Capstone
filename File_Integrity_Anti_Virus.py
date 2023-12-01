import os
import hashlib
import mysql.connector
from datetime import datetime

# Function to establish a connection to the MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='aws.connect.psdb.cloud',
            user='j2qfze5bw9iig9pkg1ap',
            password='pscale_pw_bcxKV2tNaYAExXgEkLLUhk3vf49zjCuv4rJ5FxZ0yTW',
            database='projectcapstonecybersuite'
        )
        cursor = conn.cursor()

        # Check if the timestamp column exists
        cursor.execute("SHOW COLUMNS FROM file_changes LIKE 'timestamp'")
        result = cursor.fetchone()

        if not result:
            # The timestamp column does not exist, so add it
            cursor.execute("ALTER TABLE file_changes ADD COLUMN timestamp DATETIME")
            conn.commit()

        return conn, cursor

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None

# Function to insert file change information into the database with timestamp
def insert_alert_to_database(cursor, filename, conn):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute('INSERT INTO file_changes (filename, timestamp) VALUES (%s, %s)', (filename, timestamp))
        conn.commit()
        print(f"Alert: {filename} has been modified. Alert sent to the database at {timestamp}")
    except mysql.connector.Error as e:
        print(f"Error inserting alert to the database: {e}")

def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_file_changes(directory, conn, cursor, file_hashes):
    while True:
        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                file_path = os.path.join(directory, filename)
                current_hash = calculate_file_hash(file_path)

                if file_path in file_hashes:
                    if file_hashes[file_path] != current_hash:
                        # File has been modified, send alert to the database
                        insert_alert_to_database(cursor, filename, conn)
                else:
                    file_hashes[file_path] = current_hash

        try:
            input("Press Enter to check for changes again...")

        except KeyboardInterrupt:
            print("Exiting the program.")
            if conn:
                conn.close()
            break

if __name__ == "__main__":
    directory_path = "D:\CapstoneGithub\Project-Capstone"

    conn, cursor = connect_to_database()

    # Initialize the file_hashes dictionary
    file_hashes = {}

    try:
        check_file_changes(directory_path, conn, cursor, file_hashes)

    except KeyboardInterrupt:
        print("Exiting the program.")
        if conn:
            conn.close()
