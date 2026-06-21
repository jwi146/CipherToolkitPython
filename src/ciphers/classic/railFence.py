#encrypt by distributing each character across a number of rails then concatenate
def encrypt (plaintext:str, noOfRails: int):
    #strip the spaces 
    plaintext = plaintext.replace(" ", "")
    rails = [[] for _ in range (noOfRails)] #create a list of empty lists
    direction = 1 #1 moving down, -1 moving up
    currentRail = 0
    
    for char in plaintext:
        
        #add current char to current rail
        rails[currentRail].append(char) 
        
        
        currentRail += direction
        
        if currentRail == 0 or currentRail== noOfRails-1:
            direction *= -1
    
    return ''.join(''.join(rail) for rail in rails)

#decrypt the ciphertext by simulating the zigzag and splitting the chars
def decrypt(ciphertext: str, noOfRails:int):
    ciphertext = ciphertext.replace(" ","")
    rails = [[] for _ in range (noOfRails)] #create a list of empty lists
    direction = 1 #1 moving down, -1 moving up
    currentRail = 0
    n = len(ciphertext)
    
    #first simulate rail to find out the indexes
    pattern = []
    
    #same loop as encrypt
    for char in ciphertext:
        #add current rail to pattern instead of char
        pattern.append(currentRail)

        currentRail += direction
        
        if currentRail == 0 or currentRail== noOfRails-1:
            direction *= -1
        
   # count how many chars go on each rail
    rail_lengths = [pattern.count(i) for i in range(noOfRails)]

    # slice ciphertext into chunks for each rail
    index = 0
    for i in range(noOfRails):
        rails[i] = list(ciphertext[index : index + rail_lengths[i]])
        index += rail_lengths[i]
        
    #read back zigzag order
    railIters = [iter(rail) for rail in rails]
    result = []
    for rail_no in pattern:
        result.append(next(railIters[rail_no]))
    
    
    #return plaintext
    return ''.join(result)
    
    
    
    