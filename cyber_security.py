#cryptography fun tasks with My fab Arshil noor Sir...
#BCA first year Technical Assingment 
# name = Adarsh Kumar
# Enrollment_no = 20241187

import random
import string
char = " " + string.ascii_letters + string.digits + string.punctuation
char = list(char)
key = char.copy()
random.shuffle(key)
# now we do Encryption process:
plain_text = input("Enter Your Message: ")
cipher_text = " "
for letter in plain_text:
    index = char.index(letter)
    cipher_text += key[index]
print(f"Original Message is: {plain_text}")
print(f"Encrypted text is: {cipher_text}")
# now we will do Decryption process:
cipher_text = input("Enter the Encrypted Message: ")
plain_text = " "
for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]

print(f"Encrypted Message is: {cipher_text}")
print(f"Original text is: {plain_text}")