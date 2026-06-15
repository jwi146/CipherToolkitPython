#encrypt via replacing each character with the corresponding character of the keyword
def encrypt (plaintext:str, key: str):
    key = key.lower()
    ciphertext = []
    
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a') #bound to either upper or lower case ASCII values
            charPos
        