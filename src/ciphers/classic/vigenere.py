#perform the encryption using a key word as the shift
def encrypt(plaintext: str, keyword: str ):
    ciphertext=[]
    key = keyword.lower()
    keyIndex = 0
    
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[keyIndex % len(key)]) - ord('a')#convert current key letter into is alphabet value between 0-25 
            base = ord('A') if char.isupper() else ord('a') #base and shifted act the same as caesar cipher
            shifted = (ord(char)-base + shift) % 26 + base
            ciphertext.append(chr(shifted))
        else:
            ciphertext.append(char)
    
    return ''.join(ciphertext)
            
#decrypt function by doing encrypt with negative shift
def decryption (ciphertext: str, keyword: str):
    key = keyword.lower()
    