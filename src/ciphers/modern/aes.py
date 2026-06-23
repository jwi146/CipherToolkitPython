#perform AES-CBC encryption with the help of the cryptography library 

#imports
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os

#encrypt using CBC mode and passphrase
def encrypt (plaintext:str, passphrase:str, keysize:int):
    
    #convert key size to bytes
    keySize = keysize//8
    
    #generate a random salt for passphrase
    salt = os.urandom(16)
    
    #derive the key from the passphrase using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = keySize,
        salt = salt,
        iterations = 100000
    )
    
    key = kdf.derive(passphrase.encode())
    
    #encode plaintext into bytes
    plaintextBytes = plaintext.encode()
    
    #pad plaintext to multiple of 16 using PKCS7
    
    padder = padding.PKCS7(128).padder() #create the padder (128-bit, 16 bytes)
    padded = padder.update(plaintextBytes) #add plaintext to padder
    padded += padder.finalize() #finish padding appending any remaining bytes
    
    #generate the random IV
    IV = os.urandom(16)
    
    #creates AES-CBC cipher with key and IV
    cipher = Cipher(
        algorithms.AES(key), modes.CBC(IV)
    )
    
    #create encryptor
    encryptor = cipher.encryptor()
    
    #perform encryption
    ciphertext = encryptor.update(padded)
    ciphertext += encryptor.finalize()
    
    return (salt + IV + ciphertext).hex()
    
    