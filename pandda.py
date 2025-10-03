import pandas as pd
dataa = {
    "cars": ["volvo", "bmw", "swift"],
    "dates": [1,2,4],
    "some": ["hero", "sp", "dr"]
}
vae = pd.DataFrame(dataa)
print(vae)
# a = [2,3,4]
# by = pd.Series(a, index = ['x', 'y', 'z'])
# print(by)
# print(by["y"])

# datas = {
#     "day1": [120, 43],
#     "day2": [160,44],
#     "day3": [180, 87]
# }
# some = pd.DataFrame(datas)
# print(some)

# dictt ={
#     "Calories": [400, 500,610],
#     "duration": [23,6,7]
# }
# df = pd.DataFrame(dictt)
# print(df.loc[[0]])
# print(df.loc[[0, 1]])

# enter_data = {
#     "name": ["anmol", "ritik", "abhi", "romon", "elon"],
#     "calories": [320, 300, 440, 450, 380],
#     "duration": [2,3,2,5,6],
#     "gain": [1, 4, 2, 2, 1]
# }
# close = pd.DataFrame(enter_data, index =["Day1", "Day2", "Day3", "Day4", "Day5"])
# print(close)
# print(close.loc[["Day1", "Day2"]])


# doct = {
#     "duration":{
#         "0": 60,
#         "1": 64,
#         "3": 56,
#         "4": 70,
#         "5": 59
#     },
#     "pulse": {
#         "0": 79,
#         "1": 120,
#         "3": 98,
#         "4": 87,
#         "5": 67  
#     },
#     "calories": {
#         "0": 400,
#         "1": 390,
#         "3": 370,
#         "4": 490,
#         "5": 470
#     }
# }
# pdd = pd.DataFrame(doct)
# print(pdd)
# def to_camel_case(text):
#     print(text)
# text_in = input("enter your msg: ")
# # to_camel_case(text_in)
# print(text_in)

# def to_camel_case(text):
#     print(text)
# ttext = input("enter your msg: ").title()
    
# to_camel_case(ttext)
# x = pd.read_csv('vgsales.csv')
# print(x)