# def checkp(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n **0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# def findp(lower, upper):
#     primes = []
#     for num in range(lower, upper+1):
#         if checkp(num):
#             primes.append(num)
#     return primes
# lower = int(input("enter your upper number: "))
# upper = int(input("enter your base number: "))
# primes = findp(lower,upper)
# print("prime no between", lower, "and", upper, "is: ")
# print(primes)