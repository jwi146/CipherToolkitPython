#imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

#perform DES encryption

def encrypt(plaintext:str, passphrase:str):
    
    #generate random salt
    salt = os.urandom(8)
    
    #dervice the key from passphrase (same as AES but with fixed length)
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 8,
        salt = salt,
        iterations = 100000
    )
    
    key = kdf.derive(passphrase.encode())
    
    