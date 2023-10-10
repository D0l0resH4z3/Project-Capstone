# This program will generate strong passwords with the length of the user`s choice and save passwords with username in a text file
import string
import secrets

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    
    password_chars = []

    # Generate each character of the password one by one
    for _ in range(length):
        password_chars.append(secrets.choice(characters))

    # Join the characters to form the password
    password = ''.join(password_chars)

    return password

def save_password(username, password):
    with open("passwords.txt", "a") as file:
        file.write(f"Username: {username}, Password: {password}\n")

def main():
    print("Password Manager")
    while True:
        print("\nOptions:")
        print("1. Generate a new password")
        print("2. Save a password")
        print("3. Quit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            password_length = int(input("Enter the length of the password: "))
            if password_length < 8:
                print("Password length should be at least 8 characters for security.")
            else:
                password = generate_password(password_length)
                print("Generated Password:", password)
        
        elif choice == "2":
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            save_password(username, password)
            print("Password saved successfully!")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()