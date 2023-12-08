import string
import time

def caesar_cipher(text, shift, action):
    result = []
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            if action == "encode":
                char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif action == "decode":
                char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                char = char.upper()
        result.append(char)
    return ''.join(result)

def vigenere_cipher(text, key, action):
    result = []
    key_length = len(key)
    for i, char in enumerate(text):
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            key_char = key[i % key_length].lower()

            if action == "encode":
                shift = (ord(char) + ord(key_char) - 2 * ord('a')) % 26
            elif action == "decode":
                shift = (ord(char) - ord(key_char) + 26) % 26

            char = chr(shift + ord('a'))
            if is_upper:
                char = char.upper()

        result.append(char)
    return ''.join(result)

def main(method, action, text, shift=None, key=None):
    if method == "caesar":
        if shift is None:
            print("Shift value is required for the Caesar cipher.")
            return None
        result = caesar_cipher(text, shift, action)
    elif method == "vigenere":
        if key is None:
            print("Key is required for the Vigenere cipher.")
            return None
        result = vigenere_cipher(text, key, action)
    else:
        print(f"Invalid method: {method}. Please choose 'caesar' or 'vigenere'.")
        return None

    print(f"Result: {result}")
    time.sleep(5)  # Add a sleep of 5 seconds

if __name__ == "__main__":
    method = input("Choose an encryption method (Caesar/Vigenere): ").strip().lower()
    action = input("Enter 'encode' to encode or 'decode' to decode: ").strip().lower()
    text = input("Enter the text: ")

    if method == "caesar":
        shift = int(input("Enter the shift value: "))
        main(method, action, text, shift=shift)
    elif method == "vigenere":
        key = input("Enter the key: ")
        main(method, action, text, key=key)
