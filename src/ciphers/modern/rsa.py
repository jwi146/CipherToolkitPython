#imports 
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

#generate public/private keys
def generateKeys(privateKeyPath, publicKeyPath):
    
    #generate 2048-bit RSA private key
    privateKey = rsa.generate_private_key (
        public_exponent= 65537, #standard val
        key_size= 2048
    )
    
    #dervive public from private
    publicKey = privateKey.public_key()
    
    #save the keys to a file
    
    #save private key
    
        


#encrypt plaintext



#decrypt plaintext