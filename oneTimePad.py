#This is a snippet to encrypt & decrypt onetimepads
#note that onetimepads can be decrypted only when you have the key
#please insert all strings in uppercase

from string import ascii_uppercase

def encrypt(message, key):
    alpha = ascii_uppercase
    #assigning the alphabet to a variable
    cypher = []
    #this will be the encrypted cypher

    for x in range(len(message)):
        messageCharIndex = alpha.index(message[x])
        keyCharIndex = alpha.index(key[x])
        #getting the place of both characters on which they stand in the alphabet == index (with A being 0)
        cypher.append(alpha[(messageCharIndex + keyCharIndex) % 26])
        #adding the indexes and doing modulo 26 because there are 26 numbers in alphabet
        #--> appending chars of alphabet from the index we got by subtracting

    return "".join(cypher)

def decrypt(cypher, key):
    alpha = ascii_uppercase
    #assigning the alphabet to a variable
    message = []
    #this will be the decrypted message

    for x in range(len(cypher)):
        cypherCharIndex = alpha.index(cypher[x])
        keyCharIndex = alpha.index(key[x])
        #getting the place of both characters on which they stand in the alphabet == index (with A being 0)
        message.append(alpha[(cypherCharIndex - keyCharIndex) % 26])
        #subtracting the indexes and doing modulo 26 because there are 26 numbers in alphabet
        #--> appending chars of alphabet from the index we got by subtracting

    return "".join(message)

if __name__ == "__main__":
    encMessage = "CRYPTOISFUN"
    #insert message to be encrypted here

    decCypher = "UFJKXQZQUNB"
    #insert cypher to be decrypted here

    key = "SOLVECRYPTO"
    #insert key here


    message = decrypt(decCypher,key)
    #this is the decrypted message
    cypher = encrypt(message, key)
    #this is the encrypted cypher

    print("Your decrypted message: " + message + "\nYour encrypted cypher: " + cypher)
    