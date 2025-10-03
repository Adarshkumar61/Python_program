def calculator():
    user = float(input(f"Enter your 1st number: "))
    op = input(f"What do u want to do(+, -, *, /) : ")
    user1= float(input(f"Enter your 2nd number: "))
    if op == "+" :
        summ = user + user1
        print(f"The sum of {user} and {user1} is: ", summ)
    elif op == "-" :
        minus = user - user1
        print(f"The substraction of {user} and {user1} is: ", minus)
    elif op == "*" :
        mul = user * user1
        print(f"The multipication of {user} and {user1} is: ", mul)
    elif op == "/" :
        if user1 == 0:
            print("2nd entry cant be zero")
        else:
            divide = user/user1
            print(f"The division of {user} and {user1} is: ", divide)
    else:
        print("Invalid!")
calculator()
# def calc():
#     x = float(input("enter your first number: "))
#     opp = input("What do you want to do(+, -, *, /): ")
#     y = float(input("enter your Secodnd number: "))
#     if opp == "+":
#         print(f"the sum OF {x} AND {y} is: {x+y}")
#     elif opp == "-:":
#         print(f"The substraction of {x} and {y} is: {x-y}")
#     elif opp == "*":
#         print(f"The multiplication of {x} anf {y} is: {x*y}")
#     elif opp == "/":
#         if y == 0:
#             print("2nd input cant be zero!")
#         else:
#             print(f"The division of {x} and {y} is: {x/y}")
#     else:
#         print("Invalid operator")
# calc()
# def ca():
#     x = float(input("enter your first number: "))
#     oo = input("What do you want to do(+, -, *, /): ")
#     y = float(input("enter your Second number: "))
#     if oo == "+":
#         print(f"The addition of {x} and {y} is: {x + y}")
#     elif oo == "-":
#          print(f"The Substraction of {x} and {y} is: {x - y}")
#     elif oo == "*":
#         print(f"The multiplication of {x} and {y} is: {x * y}")
#     elif oo == "/":
#         if y == 0:
#             print("Input second cant be zero")
#         else:
#             print(f"The division of {x} and {y} is: {x/y}")            
#     else:
#         print("Invalid operator")
# ca()
