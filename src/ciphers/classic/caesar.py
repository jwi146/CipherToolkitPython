#encryption function
def encrypt (plaintext: str, shift: int = 3) -> str:
    ciphertext = []
    
    #loop through the text and calculate and perform the shift
    for char in plaintext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a') #bound to either upper or lower case ASCII values
            shifted = (ord(char)-base + shift) % 26 + base #convert to a number between 0-25, add the shift and wrap around at 26
            ciphertext.append(chr(shifted))
        else:
            ciphertext.append(char)
    
    return ''.join(ciphertext)

#decrypt by calling encrypt with a negative shift
def decrypt(plaintext: str, shift: int = 3) -> str:
    return encrypt(plaintext, -shift)           