import string
from time import sleep

alphabet = string.ascii_lowercase 

def decrypt():
    
    print("Welcome to Caesar Cipher Decryption.\n")
    encrypted_message = input("Enter the message you would like to decrypt: ").strip()
    print()
    key = int(input("Enter key to decrypt: "))
    
    decrypted_message = ""

    for c in encrypted_message:

        if c in alphabet:
            position = alphabet.find(c)
            new_position = (position - key) % 26
            new_character = alphabet[new_position]
            decrypted_message += new_character
        else:
            decrypted_message += c

    print("\nDecrypting your message...\n")
    sleep(2) 
    print("Stand by, almost finished...\n")
    sleep(2) 
    print("Your decrypted message is:\n")
    print(decrypted_message)

decrypt()


#Exercise Task #5:
#Given an encrypted text t and value s. Write an algorithm, 
#that will decrypt the text by moving each letter by s numbers in an alphabet. 
#For example if the input is a and s is equal to 3, the algorithm must return d. (a,b,c,d)