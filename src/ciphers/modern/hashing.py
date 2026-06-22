import hashlib

#hasing function, take text and desired algorithm, hash and return the digest
def hashText (text:str, algorithm):
    
    #encode text to bytes
    textInBytes = text.encode()
    
    try:
        #create the hash using inputted algorithm
        hashObj = hashlib.new(algorithm)
        hashObj.update(textInBytes)
        
        #return hash digest
        return hashObj.hexdigest()
    
    except ValueError:
        raise ValueError(f"Unsupported hash algorithm: {algorithm}")
    
    