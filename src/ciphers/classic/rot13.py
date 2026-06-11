from ciphers.classic.caesar import encrypt, decrypt 

#calling rot13 twice returns original plaintext
def rot13 (plaintext: str):
    
    return encrypt(plaintext, 13)