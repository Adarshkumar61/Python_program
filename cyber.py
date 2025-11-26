import random
import string

char = " " + string.ascii_letters + string.digits + string.punctuation
char = list(char)
keyy = char.copy()
random.shuffle(keyy)

# now we will write encryption process:

plain_text = input("Enter your Message: ")
cipher_text = " "
for letter in plain_text:
    index = char.index(letter)
    cipher_text += keyy[index]
print(f"Original msg is: {plain_text}")
print(f"Encrypted Message is: {cipher_text}")

# # now for decryption process:

cipher_text = input("Enter the Encrypted Message for Plain text: ")
plain_text = " "
for letter in cipher_text:
    index = keyy.index(letter)
    plain_text += char[index]
    
print(f"Encrypted Msg is: {cipher_text}")
print(f"Plain Text is: {plain_text}")
# import random
# import string
# x = " " + string.ascii_letters + string.digits + string.punctuation
# x = list(x)
# y = x.copy()
# random.shuffle(y)
# abb = input("Emter your Message: ")
# b = " "
# for L in abb:
#     index = x.index(L)
#     b += y[index]
    
# print(f"your encrypted Message is: {b}")

# b = input("Enter the encrypted Messge: ")
# abb = " "
# for L in b:
#     index = y.index(L)
#     abb += x[index]
# print(f"Your Original message is: {abb}")
