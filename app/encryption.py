from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
import os

# Function to encrypt data using AES encryption
def encrypt_data(data):
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(16)   # Initialization Vector (IV)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    encryptor = cipher.encryptor()

    # Padding the data to be compatible with block cipher
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return iv, encrypted_data, key

# Function to decrypt data
def decrypt_data(iv, encrypted_data, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()

    unpadded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the data after decryption
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(unpadded_data) + unpadder.finalize()
    return data
