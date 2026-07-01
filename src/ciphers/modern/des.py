#imports
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import os

#perform DES encryption

def encrypt(plaintext:str, passphrase:str):
    
    #generate random salt
    salt = os.urandom(8)
    
    #derive the key from passphrase
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 8,
        salt = salt,
        iterations = 100000
    )
    
    key = kdf.derive(passphrase.encode())
    
    #encode plaintext
    plaintextBytes = plaintext.encode()
    
    #pad the plaintext to multiple of 8 bytes
    padded = pad(plaintextBytes, DES.block_size)
    
    #generate random IV
    IV = os.urandom(8)
    
    #create DES-CBC cipher using the key and IV
    cipher = DES.new(key, DES.MODE_CBC, IV)
    
    #perform encryption
    ciphertext = cipher.encrypt(padded)
    
    return (salt + IV + ciphertext).hex()


#decrypt

def decrypt(ciphertext:str, passphrase:str):
    
    #decode the hex string 
    ciphertext = bytes.fromhex(ciphertext)
    
    #split the ciphertext into salt, IV and text
    salt = ciphertext[:8]
    IV = ciphertext[8:16]
    ciphertext = ciphertext[16:]
    
    #derive the same key
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = 8,
        salt = salt,
        iterations = 100000
    )
    
    key = kdf.derive(passphrase.encode())
    
    #create the cipher 
    cipher = DES.new(key, DES.MODE_CBC, IV)
    
    #perform decryption
    decrypted = cipher.decrypt(ciphertext)
    
    #unpad the result
    unpadded = unpad(decrypted, DES.block_size)
    
    return unpadded.decode()