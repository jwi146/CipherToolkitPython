#Temporary main for testing ciphers
"""
#caesar cipher test

from ciphers.classic.caesar import encrypt, decrypt

message = input('Please enter your plaintext: ')
shift = int(input('Please enter the shift: '))
encrypted = encrypt(message, shift)
decrypted = decrypt(encrypted, shift)

print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

#rot13 testing
from ciphers.classic.rot13 import rot13 

message = input('Please enter your plaintext: ')

encrypted = rot13(message)
decrypted = rot13(encrypted)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

#vigenere testing
from ciphers.classic.vigenere import encrypt, decrypt

message = input('Please enter your plaintext: ')
keyword = input('Please enter your keyword: ')

encrypted = encrypt(message, keyword)
decrypted = decrypt (encrypted, keyword)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

#substituition test
from ciphers.classic.substitution import encrypt, decrypt

plaintext = input("Please enter your plaintext: ")
key = input("Please enter your key: ")

encrypted = encrypt(plaintext, key)
decrypted = decrypt(encrypted, key)

print(f"Original:  {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")


#test rail fence
from ciphers.classic.railFence import encrypt, decrypt

plaintext = input("Please enter your plaintext: ")
noOfRails = int(input("Please enter the number of rails: "))

encrypted = encrypt(plaintext, noOfRails)
decrypted = decrypt (encrypted, noOfRails)

print(f"Original:  {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")


# testing hashing
from ciphers.modern.hashing import hashText

text = input("Please enter your plaintext: ")
algorithm = input("Please enter the algorithm (md5/sha1/sha256/sha512): ")

print(f"Hash: {hashText(text, algorithm)}")
"""

from ciphers.modern.aes import encrypt, decrypt

plaintext = input("Please enter your plaintext: ")
passphrase = input("Please enter your passphrase: ")
keysize = int(input("Enter key size (128/192/256): "))

encrypted = encrypt(plaintext, passphrase, keysize)
decrypted = decrypt(encrypted, passphrase, keysize)

print(f"Original:  {plaintext}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")