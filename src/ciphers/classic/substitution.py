#encrypt via replacing each character with the corresponding character of the keyword
def encrypt (plaintext:str, key: str):
    key = key.lower()
    ciphertext = []
    
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                charUpper = True
            else:
                charUpper = False
            
            textPos = ord(char.lower()) - ord('a') 
            replacement = key[textPos]
            
        
            
