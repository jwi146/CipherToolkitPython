#temporary main for testing ciphers

#caesar cipher test
"""
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
"""
#vigenere testing
from ciphers.classic.vigenere import encrypt, decrypt

message = input('Please enter your plaintext: ')
keyword = input('Please enter your keyword: ')

encrypted = encrypt(message, keyword)
decrypted = decrypt (encrypted, keyword)

print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")
