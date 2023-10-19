import string

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
    action = input("Enter 'encode' to encode or 'decode' to decode: ").strip().lower()
    if action not in ['encode', 'decode']:
        print("Invalid action. Please enter 'encode' or 'decode'.")
        return

    text = input("Enter the text: ")
    key = input("Enter the key: ")

    encoded_text = vigenere_cipher(text, key, action)
    print(f"Result: {encoded_text}")

if __name__ == "__main__":
    main()
