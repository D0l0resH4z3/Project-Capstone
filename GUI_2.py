
from hypercli import hypercli
import getpass
import subprocess
import mysql.connector


# Hardcoded usernames and passwords
user_credentials = {
    "user1": "password1",
    "user2": "password2",
    # Add more usernames and passwords as needed
}

def login():
    print("Login to access the main menu.")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # Check if the entered username and password are valid
    if username in user_credentials and user_credentials[username] == password:
        print("Login successful!\n")
        return True
    else:
        print("Invalid username or password. Please try again.\n")
        return False

# Add the login prompt before the main menu
while not login():
    pass  # Continue prompting for login until successful

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
# Establish a connection to the database
conn, cursor = connect_to_database()

# create an instance of hypercli
cli = hypercli()


# configure the in#stance
cli.config["banner_text"] = "CyberSuite Tools"
cli.config["intro_title"] = "Intro"
cli.config["intro_content"] = "The Ultimate Cyber tools for your needs!"
cli.config["show_menu_table_header"] = True
cli.config["show_exit"] = False

cli.link("Main Menu", "Tools Menu")


# Initialize the file_hashes dictionary
file_hashes = {}
while True:
    
    @cli.entry(menu="Main Menu", option="User Documentation")
    def user_documentation():
        subprocess.run(['python', 'user_documentation.py'])
        
    @cli.entry(menu="Main Menu", option="Install Necessary Libraries")
    def install_libraries():
        subprocess.run(['python', 'install_libraries.py']) 
    
    @cli.entry(menu="Main Menu", option="Files")
    def Show_files():
        subprocess.run(['python', 'Show_files.py'])     
           
    @cli.entry(menu="Main Menu", option="Quit ✗")
    def quit_program_1():
        cli.exit()
        exit()
    
    
    
    
    @cli.entry(menu="Tools Menu", option="Password Generator")
    def Password_Generator():
        subprocess.run(['python', 'Password_Generator.py'])
    

    @cli.entry(menu="Tools Menu", option="String Encoder/Decoder")
    def encoderdecoder():
        subprocess.run(['python', 'encoderdecoder.py'])
    

    @cli.entry(menu="Tools Menu", option="Image Metadata Remover")
    def metadata_removal():
        subprocess.run(['python', 'metadata_removal.py'])
        

    @cli.entry(menu="Tools Menu", option="Key Logger")
    def keylogger():
        subprocess.run(['python', 'keylogger.py'])
        

    @cli.entry(menu="Tools Menu", option="Port Scanner")
    def Port_scanner():
        subprocess.run(['python', 'Port_scanner.py'])
        

    @cli.entry(menu="Tools Menu", option="Web Scraper")
    def Web_scraper():
        subprocess.run(['python', 'Web_scraper.py'])
        
    @cli.entry(menu="Tools Menu", option="Encryption / Decryption")
    def Encryption_or_Decryption():
        subprocess.run(['python', 'Encryption_or_Decryption.py'])    
    

    @cli.entry(menu="Tools Menu", option="Anti-Virus Scan | File Integrity Check")
    def File_Integrity_Anti_Virus():
        subprocess.run(['python', 'File_Integrity_Anti_Virus.py'])
        
    @cli.entry(menu="Tools Menu", option="Quit ✗")
    def quit_program_2():
        cli.exit()
        exit()
    
    

# Run the cli
    cli.run()