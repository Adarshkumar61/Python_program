
# def area(l, b, h):
#     areaa = l * b + h
#     print(areaa)
# area(2, 3, 1)    
# area(5, 6, 1)
# area(5, 8, 1)
# area(2, 2, 1)

# def cov(usd_val):
#     inr_val = usd_val * 87
#     print(usd_val,"USD =", inr_val,"INR")
# cov(2)    

# #craete a fn who takes a input and greet hello - name
# def greet():
#     name = input("enter your name: ")
#     print(f"hello {name}")
# greet()    

# #created a fn who takes two input and return their sum
# def add_numbers():
#     a = float(input("First number is: "))
#     b = float(input("Second number is: "))
#     print(f"the Sum is: {a + b}")
# add_numbers()  

# #created a fn who takes a input and give odd/even 
# def is_even():
#     num = float(input("enter your number: "))
#     if num %2 == 0:
#         print(f" {num} is even")
#     else:
#         print(f"{num} is odd") 
# is_even()   
#         
#craete a fn who takes a input and give the sq number
# def square():
#     num = int(input("enter your number: "))
#     num *= num
#     print(f"the square is: {num}")
# square()

# def full_name():
#     fname = str(input("enter your first name: "))
#     lname = str(input("enter your lastt name: "))
#     print(f"The full name is {fname} {lname}")
# full_name()    

# def cal_avg():
#     numbers = input("enter a list of numbers: ")
#     numbers = [float(num) for num in numbers.split()]
#     avrage = sum(numbers) / len(numbers)
#     print(f"the avg is: {avrage:.2f}")
# cal_avg()    

# num = int(input("Enter your number: "))
# if num % 2 == 0:
#     print(f"{num} is even number")
# else:
#     print(f"{num} is odd number")

# def fact(n):
#     if n<=1:
#         return "Number is neither prime nor composite"
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return "Number is composite"
#     return "Number is prime"
# num = int(input("Enter an integer: "))
# print(fact(num))

# import calendar
# year = int(input("Enter year: ")) 
# month = int(input("ENter your month: "))
# date = int(input("Enter your date: "))
# cal = calendar.month(year, month, date)
# print(cal)


# a = 5
# b = 6
# a,b=b,a
# print("after swapping: ")
# print("a=", a)
# print("b=", b)

# num = float(input("Enter your number: "))
# if num > 0:
#     print(f"{num} is positive")
# elif num == 0:
#     print(f"{num} is neither positive nor negative")
# else:
#     print(f"{num} is negative number")

#prime number within an interval 
# def check_prime(n):
#     if n<= 1:
#         return False
#     for i in range(2, int(n **0.5)+1):
#         if n % i ==0:
#             return False
#     return True

# def find_prime(lower, upper):
#     primes=[]
#     for num in range(lower, upper+1):
#         if check_prime(num):
#             primes.append(num)
#     return primes

# lower = int(input("Enter your base number: "))
# upper = int(input("Enter your Upper number: "))
# primes = find_prime(lower, upper)
# print("prime num bw", lower, "and", upper, "are: ")
# print(primes)
