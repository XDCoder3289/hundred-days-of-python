# This code will replicate the caesar cipher

# There should be an option to encrypt
# There should be an option to decrypt
# The program should ask for the shift
# decrypt = input("Please enter what you want to decrypt: ")
# test
from asciii import logo

print(logo)

task = int(input("Do you want to (1)encrypt or (2)decrypt: "))
shift = int(input("How much do you want the shift to be: "))
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



if task == 1:
    def cipher_encrypt():
        encrypt = input("Please enter what you want to encrypt: ")
        word = ''
        spaces = [i for i,x in enumerate(encrypt) if x == " "]
        encrypt = encrypt.replace(" ", "").lower()
        
        for letter in encrypt:
            index = alphabets.index(letter)
            new_letter = index + shift
            if new_letter >= 26:
                new_letter = abs(26 - new_letter)
                  
            word += alphabets[new_letter]
        
        for space in spaces:
            word = word[:space] + ' ' + word[space:]  
        
        print(word)
    cipher_encrypt()

if task == 2:
    def cipher_decrypt():
        
        decrypt = input("Please enter what you want to decrypt: ")
        word = ''
        spaces = [i for i,x in enumerate(decrypt) if x == " "]
        decrypt = decrypt.replace(" ", "").lower()
        
        for letter in decrypt:
            index = alphabets.index(letter)
            new_letter = index - shift
            if new_letter >= 26:
                new_letter = abs(26 - new_letter)
            word += alphabets[new_letter]
        
        for space in spaces:
            word = word[:space] + ' ' + word[space:]  
        
        print(word)
    cipher_decrypt()

