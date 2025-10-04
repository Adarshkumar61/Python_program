
import random
import numpy as np
# rock paper
# def rps():
#     choices = ["rock", "paper", "scissors"]
#     com_choice= random.choice(choices)
#     user_choice = input("enter your word: ")
#     if com_choice == user_choice:
#        print("Its a tie")
#     elif(user_choice == "rock" and com_choice == "scissor") or \
#         (user_choice == "scissor" and com_choice == "paper") or \
#         (user_choice == "paper" and com_choice == "rock"):
#        print("you win..")
#     else:
#         print("computer win..", com_choice)
#     ask = input("want to play more?").lower()
#     if ask == "yes":
#         rps()
# rps()        
    
# rps()
# import requests
# API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
# response = requests.get(API_URL)
# rates = response.json()["rates"]

# amount = float(input("Enter amount in USD: "))
# currency = input("Enter currency code (e.g., INR, EUR): ").upper()

# if currency in rates:
#     print(f"{amount} USD = {amount * rates[currency]} {currency}")
# else:
#     print("Currency not supported.")
# import requests
# api = "https://api.exchangerate-api.com/v4/latest/USD"
# x = requests.get(api)
# y = x.json()["rates"]
# z = float(input("ENter the amount in Usd: "))
# t = input("enter the currency code (e.g - inr , usd...): ").upper()
# if  t in y:
#     print(f"{z} Usd = {z * y[t]} {t}")
# else:
#     print("invalid country code!...")
    
    #to do program:
# tasks = []
# def add_task(task):
#     tasks.append(task)
# def view_task():
#     for i, task in enumerate (tasks, start = 1):
#        print(f"{i}. {tasks}")
# def remove_task(tasknumber):
#    try:
#        del tasks[tasknumber - 1]
#    except IndexError:
#        print("invalid!..")
# while True:
#     print("Enter 1 for Add task..")
#     print("Enter 2 for View Task..")
#     print("Enter 3 for remove Task..")
#     print("enter 4 for quit..")
#     choice = input("Enter your choice(1, 2, 3, 4): ")
#     if choice == "1":
#         task = input("Enter your task: ")
#         add_task(task)
#     elif choice == "2":
#         view_task()
#     elif choice == "3":
#         tasknumber = int(input("enter the task number to remove: "))
#         remove_task(tasknumber)
#     elif choice == "4":
#         break 
#     else:
#         print("Invalid choice.. Please choose correct option (1, 2, 3, 4)")
# class Solution:
#     def twoSum(self, nums, target):
#         num_dict = {}
#         for i, num in enumerate(nums):
#             complement = target - num
#             if complement in num_dict:
#                 return [num_dict[complement], i]
#             num_dict[num] = i

# data = {
#     "hello" "hii": "Hlw how may i help you ?",
#     "hlo": "hello how can i assist you ?",
#     "hlw":  "hello how can i assist you ?",
#     "how are you": "I'm good, thanks for asking..  what about you?",
#     "good": "Good to hear this.. How can i help you?",
#     "what is your name": "i'm Goldy(R**)",
#     "who is your owner": "my owner is Mr. Adarsh singh",
#     "who is richest man on earth": "Elon musk",
#     "who is founder of facebook": "mark juckerburg",
#     "who is ceo of google": "sunder pichai",
#     "who is pm of india": "shri Narendra damodar das modi",
#     "what can you do": "I can give basic answers like Greetings, my name and some GK, ceo and etc...",
#     "2+2": "4",
#     "tell me a joke": "your life... ☠️",
#     "tell me a dark joke": "dark humour is like food everyone can't gets it...☠️",
#     "what is the one motivaion you give": "you only have 2 options: \n 1. Either play safe and die with regrets or \n 2. Take risk and die with a story",
#     "what is the criteria to vote in india": "to vote in india you have to 18 or plus",
#     "can u solve math problems ?": "yeah bit very basic..",
#     "what is 4 * 5": "20",
#     "what is 100/5": "20",
#     "i want to start a business what should i do":"pick something research about it and just start..good luck",
#     "tell me an idea that can really go big": "sure: \n Pharmacy\n makeup for womens\n agriculture new technogies\n low rate clother with good quality",
#     "thanku": "wlcm have a nice day☺️ feel free to ask questions..",
#     "what do u think about ai": "ai is really great and it will gonna boost very much because of its capablities...",
#     "create a python program of addtion": "sure: \n def add(): \n inp = input('enter first number': )\n inp2= input('enter second number': )\n sum = inp + inp2\n print(sum)\n add())",
#     "can u recommend me a book": "hard things by hard things, this book is really good.",
#     "can u dance": "i can't, i am a virtual chatbot created By RVA , so i can only give you answers of some questions",
#     "who is highest followed person on instagram": "cristiano ronaldo is highest followed person on instgram",
#     "who is the goat of football": "cristiano and messi both are goat players..of football",
#     "choose one": "messi because he have a world cup but, cristiano is also a very high goated player respect 🫡",
#     "tell me one thing that can change my life": "just take risk and see the outcome you will never regret",
#     "can u do calculations": "yes but a little bit",
#     "can u speak": "i can't, i am a virtual chatbot created By RVA , so i can only give you answers of some questions",
#     "who created you": "i am created by RVA owner Adarsh kumar singh",
#     "what u can do that other ai can't": "for your clarification i am not an AI i am just a normal chatbot which can give answers of simple questions..",
#     "tell me another joke": "Why did the astronaut break up with his girlfriend? \n Because he needed space!",
#     "emoji": "😀😃😄😆🥹😅😂🤣🥲☺️😊😇🙂🙃😉😌😍🥰😘😗😙😚😋😛😝😜🤪🤨🧐🤓😎🥸🤩🥳🙂‍↕️😏😒🙂‍↔️😞😔😔😟😕🙁☹️😣😖😫😩🥺😢😭😤😠😡🤬🤯😳🥵🥶😶‍🌫️😱😨😰😥🤗🤔🫣🤭🫢🫡🤫🫠🤧🤤😑🫤",
#     "give me some happy emoji": "sure:\n😀😃😄 ☺️😊😇",
#     "give me some sad emoji": "sure:\n🥹😒😞😔😔",
#     "i am sad": "ohh..don't be sad 🥹\n here is a joke that make u smile and make your day better ☺️😊\n Why don't skeletons fight each other?\nBecuse they don't have the guts! 😄\nHope that gave you a laugh!"
    
# }
# def Chatbot():
#     print("Hlo wclm to RVA chatbot..".title())
#     print("don't use question mark for asking question.".title())
#     print("use correct grammer for asking question.".title())
#     while True:
        
#         inp = input("enter your message: ").lower()
#         if inp in data:
#             print("Chatbot: ", data[inp].title())
#         elif inp == "quit":
#             print(" have a nice day..☺️")
#             break
#         else:
#             print("sorry this is out of my dictionary...")
# chatbot()

#random pass generator:

# def trianglee(n):
#     for i in range(2, n+1):
#         print("*" * i)
# trianglee(5)
# import random
# import string
# def rndom_pass(leng):
#     if leng < 4:
#         return "digit should be atlest 4"
#     password = string.ascii_letters + string.digits
#     char = " ".join(random.choice(password) for i in range(leng))
#     return char

# while True:
#     leng = int(input("enter your desired length of password: "))
#     who = rndom_pass(leng)
#     print("your desired passwrod is: ", rndom_pass(leng))
#     ask = input("want to generate again ?")
#     if ask.lower() != "yes":
#         break
# print("okk exiting")


#creating a prime number checker:


# def prime_num_finder():
    
#     def check_prime(n):
#         if n < 1:
#             return False
#         for i in range (2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 return False
#             return True
    
#     def find_prime(starting, end):
#         prime_num_storage = []
#         for num in range (starting, end + 1):
#             if check_prime(num):
#                 prime_num_storage.append(num)
#         return prime_num_storage        
#     starting = int(input("Enter the starting Numbert: "))
#     end = int(input("Enter the end Number: "))
#     result = find_prime(starting, end)
#     print(f"The prime number between {starting} and {end} is ", result)
#     ask = input("want to generate again ? (yes/no)")
#     if ask == "yes":
#         prime_num_finder()
#     else:
#         print("Okk, see you next time..")

# prime_num_finder()

    
#creating a model:

# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import pandas as pd

# data = pd.read_csv('#here our csv file')

# X = data.drop('#output coloumn of csv file')
# y = data['#output column']

# X_train, y_train, X_test, y_test = train_test_split(X, y, test_size=0.2) 

# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)

# preditction = model.predict(X_test)

# score = accuracy_score(y_test, preditction)
# print(f"score: {score:.2f}")


# import pandas as pd
# from sklearn.datasets import load_iris
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import accuracy_score

# # Load the Iris dataset
# iris = load_iris()
# X = iris.data
# y = iris.target

# # Split the dataset into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# # Initialize the Decision Tree Classifier
# tewx = DecisionTreeClassifier()

# # Train the classifier
# tewx.fit(X_train, y_train)

# # Make predictions
# y_pred = tewx.predict(X_test)

# # Calculate the accuracy
# accuracy = accuracy_score(y_test, y_pred)
# print(f'Accuracy: {accuracy:.2f}')


# we willl use a algorithim which is called descision tree 
#it is come in scikit learn library
# sklearn is a package comes in scikit lear



# class bank:
#     def __init__(self, balance):
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         print("Rs", amount, "credit to your account")
#         print("Now current balance is =", self.get_bal())
        
#     def withdraw(self, amount):
#         self.balance -= amount
#         print("Rs", amount, "is debited to your account")
#         print("Now total balance is = ", self.get_bal())
        
        
#     def get_bal(self):
#         return self.balance
    
# acc1 = bank(10000)
# acc1.deposit(2000)
# acc1.withdraw(2000)


# arr = np.array([[12.0,0.24, 2.1,23.2, 423.5, 12.3], [12.0,0.24, 2.1,23.2, 423.5, 12.3]])
# narr = arr.reshape(-1)
# print(narr)


# data = {
#     'hlo': 'hii i am adarsh'
# }
# def chatbot():
#     while True:
#         user = input('Enter your message: ')
#         if user in data:
#             print('Goldy', data[user])
#         else:
#             print('not found')
#             break
# chatbot()
# def check(n, m):
#     sum  = n+m
#     # print(sum)
#     mul = n*m
#     print(mul)
# check(2, 3)
# check(3, 4)

# flake8: noqa
# import os

# # Set backend env to JAX
# os.environ["KERAS_BACKEND"] = "jax"

# import jax
# import numpy as np

# from keras import Model
# from keras import backend
# from keras import initializers
# from keras import layers
# from keras import ops
# from keras import optimizers


# class MyDense(layers.Layer):
#     def __init__(self, units, name=None):
#         super().__init__(name=name)
#         self.units = units

#     def build(self, input_shape):
#         input_dim = input_shape[-1]
#         w_shape = (input_dim, self.units)
#         w_value = initializers.GlorotUniform()(w_shape)
#         self.w = backend.Variable(w_value, name="kernel")

#         b_shape = (self.units,)
#         b_value = initializers.Zeros()(b_shape)
#         self.b = backend.Variable(b_value, name="bias")

#     def call(self, inputs):
#         return ops.matmul(inputs, self.w) + self.b


# class MyModel(Model):
#     def __init__(self, hidden_dim, output_dim):
#         super().__init__()
#         self.dense1 = MyDense(hidden_dim)
#         self.dense2 = MyDense(hidden_dim)
#         self.dense3 = MyDense(output_dim)

#     def call(self, x):
#         x = jax.nn.relu(self.dense1(x))
#         x = jax.nn.relu(self.dense2(x))
#         return self.dense3(x)


# def Dataset():
#     for _ in range(20):
#         yield (np.random.random((32, 128)), np.random.random((32, 4)))


# def loss_fn(y_true, y_pred):
#     return ops.sum((y_true - y_pred) ** 2)


# model = MyModel(hidden_dim=256, output_dim=4)

# optimizer = optimizers.SGD(learning_rate=0.001)
# dataset = Dataset()

# # Build model
# x = np.random.random((1, 128))
# model(x)
# # Build optimizer
# optimizer.build(model.trainable_variables)


# ######### Custom JAX workflow ###############


# def compute_loss_and_updates(
#     trainable_variables, non_trainable_variables, x, y
# ):
#     y_pred, non_trainable_variables = model.stateless_call(
#         trainable_variables, non_trainable_variables, x
#     )
#     loss = loss_fn(y, y_pred)
#     return loss, non_trainable_variables


# grad_fn = jax.value_and_grad(compute_loss_and_updates, has_aux=True)


# @jax.jit
# def train_step(state, data):
#     trainable_variables, non_trainable_variables, optimizer_variables = state
#     x, y = data
#     (loss, non_trainable_variables), grads = grad_fn(
#         trainable_variables, non_trainable_variables, x, y
#     )
#     trainable_variables, optimizer_variables = optimizer.stateless_apply(
#         optimizer_variables, grads, trainable_variables
#     )
#     # Return updated state
#     return loss, (
#         trainable_variables,
#         non_trainable_variables,
#         optimizer_variables,
#     )


# trainable_variables = model.trainable_variables
# non_trainable_variables = model.non_trainable_variables
# optimizer_variables = optimizer.variables
# state = trainable_variables, non_trainable_variables, optimizer_variables
# # Training loop
# for data in dataset:
#     loss, state = train_step(state, data)
#     print("Loss:", loss)

# # Post-processing model state update
# trainable_variables, non_trainable_variables, optimizer_variables = state
# for variable, value in zip(model.trainable_variables, trainable_variables):
#     variable.assign(value)
# for variable, value in zip(
#     model.non_trainable_variables, non_trainable_variables
# ):
#     variable.assign(value)

# inp = int(input('enter your number: '))
# for i in range(1, inp +1):
#     print(i, end= '')

# program to find area and circumference of circle:
# radius  = int(input("enter the radius of circle: "))
# area = 3.14 * radius * radius
# print("the area of circle is: ", area)
# circumference = 2 * 3.14 * radius
# print("the circumference of circle is: ", circumference)


# this is a pattern program:
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# # Newton-Raphson Method in Python:
# def f(x):
#     return x**3 - 3*x +2
# def df(x):
#     return 3*x**2 - 3

# def newton_rapshan_method(x0, toi = 1e-6, max_iter = 100):
#     x = x0
#     for i in range(max_iter):
#         fx = f(x)
#         dfx = df(x)
#         if dfx == 0:
#             print('Derivative zero')
#             return None
#         new = x - fx / dfx
#         if (new-x)<toi:
#             return new
#         x= new
#     return x
# root = newton_rapshan_method(2)
# print(f'root is: {root}')

x = -10
print(abs(x))

x = ([12, 23, 6, 38, 14])
print(sorted(x))