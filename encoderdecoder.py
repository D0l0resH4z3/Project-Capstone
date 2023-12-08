import string
import time

def caesar_cipher(text, shift, action):
    result = []
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            if action == "e":
                char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            elif action == "d":
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

            if action == "e":
                shift = (ord(char) + ord(key_char) - 2 * ord('a')) % 26
            elif action == "d":
                shift = (ord(char) - ord(key_char) + 26) % 26

            char = chr(shift + ord('a'))
            if is_upper:
                char = char.upper()

        result.append(char)
    return ''.join(result)

def main(method, action, text, shift=None, key=None):
    if method == "c":
        if shift is None:
            print("\nShift value is required for the Caesar cipher.")
            return None
        result = caesar_cipher(text, shift, action)
    elif method == "v":
        if key is None:
            print("\nKey is required for the Vigenere cipher.")
            return None
        result = vigenere_cipher(text, key, action)
    else:
        print(f"\nInvalid method: {method}. Please choose 'caesar' or 'vigenere'.")
        return None

    print(f"\nResult: {result}")
    time.sleep(3)  # Add a sleep of 3 seconds

if __name__ == "__main__":
    method = input("\nChoose an encryption method Caesar or Vigenere  (C/V): ").strip().lower()
    action = input("\nEnter 'E' to encode or 'D' to decode (E/D): ").strip().lower()
    text = input("\nEnter the text: ")

    if method == "c":
        shift = int(input("\nEnter the shift value: "))
        main(method, action, text, shift=shift)
    elif method == "v":
        key = input("\nEnter the key: ")
        main(method, action, text, key=key)
