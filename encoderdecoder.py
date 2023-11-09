#String encoder/decoder using Vigenère cipher encryption

import string

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

def main():
    method = input("Choose an encryption method (Caesar/Vigenere): ").strip().lower()
    if method not in ['caesar', 'vigenere']:
        print("Invalid method. Please choose 'Caesar' or 'Vigenere'.")
        return

    action = input("Enter 'encode' to encode or 'decode' to decode: ").strip().lower()
    if action not in ['encode', 'decode']:
        print("Invalid action. Please enter 'encode' or 'decode'.")
        return

    text = input("Enter the text: ")

    if method == "caesar":
        shift = int(input("Enter the shift value: "))
        result = caesar_cipher(text, shift, action)
    elif method == "vigenere":
        key = input("Enter the key: ")
        result = vigenere_cipher(text, key, action)

    print(f"Result: {result}")

if __name__ == "__main__":
    main()

