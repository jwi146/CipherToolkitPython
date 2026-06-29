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
    
#decrypt by reversing the process
def decrypt(ciphertext:str, passphrase:str, keySize:int):
    
    #convert key to bytes
    keyBytes = keySize//8
    
    #decode the hex string
    ciphertext = bytes.fromhex(ciphertext)
    
    #split the ciphertext into its components
    salt = ciphertext[:16] #first 16 is salt
    IV = ciphertext [16:32] #next 16 iv
    ciphertext = ciphertext[32:] #the rest is the text
    
    #derive the same key
    kdf = PBKDF2HMAC(
        algorithm = hashes.SHA256(),
        length = keyBytes,
        salt = salt,
        iterations = 100000
    )
    
    key = kdf.derive(passphrase.encode())
    
    #create the AES-CBC cipher using the key and iv
    cipher = Cipher(
        algorithms.AES(key), modes.CBC(IV)
    )
    
    #decrypt the cipher
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext)
    plaintext += decryptor.finalize()
    
    # unpad the text
    unpadder = padding.PKCS7(128).unpadder()
    unpadded = unpadder.update(plaintext)
    unpadded += unpadder.finalize()
    
    return unpadded.decode()