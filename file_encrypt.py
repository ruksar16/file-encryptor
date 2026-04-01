from cryptography.fernet import Fernet

# Function to generate key (run once)
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved as 'key.key'")

# Load key
def load_key():
    return open("key.key", "rb").read()

# Encrypt file
def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(filename + ".enc", "wb") as f:
        f.write(encrypted)
    print(f"File '{filename}' encrypted successfully!")

# Decrypt file
def decrypt_file(filename):
    if filename.endswith(".enc"):
        output_file = filename[:-4]
    else:
        print("Invalid encrypted file")
        return
    key = load_key()
    fernet = Fernet(key)
    with open(filename, "rb") as f:
        data = f.read()
    decrypted = fernet.decrypt(data)
    output_file = filename.replace(".enc", "")
    with open(output_file, "wb") as f:
        f.write(decrypted)
    print(f"File decrypted successfully as '{output_file}'")

if __name__ == "__main__":
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
    filename = input("Enter file name: ")
    
    if choice == 'E':
        encrypt_file(filename)
    elif choice == 'D':
        decrypt_file(filename)
    else:
        print("Invalid choice! Enter 'E' or 'D'.")

