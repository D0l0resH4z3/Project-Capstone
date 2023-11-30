import os
import hashlib

def calculate_file_hash(file_path):
    """
    Calculate the SHA-256 hash of a file.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as file:
        # Read and update hash string value in blocks of 4K
        for byte_block in iter(lambda: file.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def check_file_changes(directory):
    """
    Check for changes in all Python files in the specified directory.
    """
    for filename in os.listdir(directory):
        if filename.endswith(".py"):
            file_path = os.path.join(directory, filename)
            current_hash = calculate_file_hash(file_path)
            
            if file_path in file_hashes:
                # File already seen, check for modification
                if file_hashes[file_path] != current_hash:
                    print(f"Alert: {filename} has been modified!")
            else:
                # New file, add to the dictionary
                file_hashes[file_path] = current_hash

if __name__ == "__main__":
    directory_path = "D:\CapstoneGithub\Project-Capstone"  # Change this to the directory path you want to monitor
    file_hashes = {}      # Dictionary to store file hashes

    while True:
        check_file_changes(directory_path)

        # Optional: Adjust the sleep time based on your needs
        try:
            input("Press Enter to check for changes again...")
        except KeyboardInterrupt:
            break
