# import random
# def password():
#     user = input("Enter the Password length you want: ")
#     if user == "4":
#         rdm = random.randint(1000, 9999)
#     elif user == "5":
#         rdm = random.randint(10000, 99999)
#     elif user == "6":
#         rdm = random.randint(100000, 999999)
#     else:
#         print("sorry Max  6 length password is allowed and higher than 3 digits")
#     print("Strong password: ", rdm)
# password()

# combi = string.ascii_letters + string.digits + string.punctuation
# 
# import random
# import string
# def generator(length):
#     charr = string.ascii_letters + string.digits
#     if length < 4:
#         print("password length should atleast 4 digits..")
#         return None
#     passs = "".join(random.choice(charr) for i in range(length))
#     return passs
# length = int(input("Enter the password length: "))
# print("random password is: ", generator(length))




import random
import string
def random_pass(length):
    if length < 4:
        return "password length should atleast 4 digits.."
    char = string.ascii_letters + string.digits
    password = " ".join(random.choice(char) for i in range(length))
    return password    
while True:
    try:
        length = int(input("Enter your password length: "))
        break
    except ValueError:
        print("invalid input..")
password = random_pass(length)
print("Generated password: ", password)        


# import random
# import string
# def password_gen(length):
#     if length < 4:
#         print("password length should atleast 4 digits..")
#     character = string.ascii_letters + string.digits
#     password = "".join(random.choice(character) for i in range(length))
#     return password
# while True:
#     try:
#         length = int(input("Enter the length of your password: "))
#         break
#     except ValueError:
#         print("invalid input.. Please enter correct input")
# password = password_gen(length)
# print("Generated password is: ", password)