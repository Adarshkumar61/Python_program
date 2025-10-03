# class factory:
#     name = "BMW"
#     model = "xyz"
# s1 = factory()
# print(factory.name)   
# print(factory.model) 

# class student:
#     def __init__(self, fullname, marks):
#         self.name = fullname
#         self.marks = marks
# s1 = student("adarsh", 80)
# print(s1.name, s1.marks)
# s2 = student("hero", 99)
# print(s2.name, s2.marks)

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def avg_marks(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hii", self.name, "your avg makrs is:", sum/3)
# s1 = student("adarsh", [98, 43, 99])
# s1.avg_marks()


# class car:
#     def __init__(self, name, brand, model, nmodel):
#         self.name = name #attribute
#         self.brand = brand
#         self.model = model
#         self.nmodel = nmodel

#     def start(self):
#         print(f"{self.name} is starting")
     
#     def stock(self):
#         print(f"{self.brand} is currently out of stock")

#     def about(self):
#         print(f"{self.brand} is out of stock now but you can look {self.nmodel}")
# car1 = car("Tesla", "EV", "X2", "A4")
# car1.start()
# car1.stock()
# car1.about()

# class acc:
#     def __init__(self, balance, accno):
#        self.balance = balance
#        self.accno = accno

#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs", amount, "was debited")
#         print("now total balance = ", self.get_bal())

#     def credit(self, amount):
#         self.balance += amount
#         print("Rs", amount, "is credited")
#         print("Now total balance is=",self.get_bal())

#     def get_bal(self):
#         return self.balance

# acc1 = acc(2000, 23434)

# acc1.debit(500)
# acc1.credit(700)
# acc1.credit(1000)

# class car:
#     @staticmethod
#     def start():
#         print("car has started..")
        
#     @staticmethod
#     def stop():
#         print("car stopped..")
        
        
# class toyota(car):
#    def __init__(self, name):
#        self.name = name
       
# class fortuner(toyota):
#     def __init__(self, typee):
#         self.typee = typee
# car1 = fortuner("xuv")
       

class company:
    def __init__(self, name, model, price, nprice):
        self.name = name
        self.model = model
        self.price = price
        self.nprice =nprice
        
    def toyota(self):
        print(f"Car name is {self.name} and model is {self.model}")
        print(f"price of this car is: {self.price} and it goes to {self.nprice}")

    def suzuki(self):
        print(f"Car name is {self.name} and model is {self.model}")
        print(f"Car price is {self.price} and it goes to {self.nprice}")

    def bmw(self):
        print(f"Car name is {self.name} and model is {self.model}")
        print(f"Car price is {self.price}")

    def mercedes(self):
        print(f"Car name is {self.name} and model is {self.model}")
        print(f"Car price is {self.price}")

    def lambo(self):
        print(f"Car name is {self.name} and model is {self.model}")
        print(f"Car price is {self.price}")

    def tata(self):
        print(f"Car name is {self.name} and model is {self.model}")
        print(f"Car price is {self.price}")

    def tesla(self):
        print(f"Car name is {self.name} and model is {self.model}")
        print(f"C   ar price is {self.price}")


car1 = company("innova", "X5", "17Lakh", "59Lakh")
# car1.toyota()

# car2 = ("invalid")
car1.tesla()