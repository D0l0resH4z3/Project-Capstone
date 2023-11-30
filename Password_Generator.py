# This program will generate strong passwords with the length of the user`s choice and save passwords with username in a text file
# Import necessary modules
import string
import secrets

# Function to generate a strong password of the given length
def generate_password(length):
    # Define the set of characters to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password_chars = []  # Initialize an empty list to store password characters

    # Generate each character of the password one by one
    for _ in range(length):
        password_chars.append(secrets.choice(characters))

    # Join the characters to form the password
    password = ''.join(password_chars)

    return password

# Function to save a username and password in a text file
def save_password(username, password):
    with open("passwords.txt", "a") as file:
        # Write the username and password 
        file.write(f"Username: {username}, Password: {password}\n")


if __name__ == "__main__":
    print("\nPassword Manager")
    while True:
        print("\nOptions:")
        print("1. Generate a new password")
        print("2. Save a password")
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
            save_password(username, password)
            print("Password saved successfully!")
        
        elif choice == "0":
            print("\nExiting the Password Generator.")
            break
        
        else:
            print("Invalid choice !!!")