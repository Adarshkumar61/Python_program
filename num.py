from numpy import random
import numpy as np
# x = np.array([1,10,13,23,34,45,54])
# # print(x[0:6:3])
# print(x[2] + [3])
# # print(type(x))

# # creating a 0-D array :
# arr = np.array(42)
# print(arr)

# # creating a 2d array:
# y = np.array([[1,2,3], [4,5,6]])
# print(y)

# data = np.array([i for i in range(50)])
# print(data[10:20])
# x = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
# print(x[0, 0, -1])
# here 0: index 0 list, 0 : means o index list of list, -1: negative indexing result: 3

# arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
# print(arr[1, 4])

# arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11,12,13,14,15]])
# print(arr[0:3,2])
# print(arr[0:3, 1:4])

# arr = np.array([1,2,3,4,5])
# x = arr.copy()
# # arr[0] = 42
# # print(arr)
# print(x)
# arr = np.array([1,2,3,4,5])
# x = arr.view()
# x[0] = 32
# print(arr)
# # print(x)

# arr = np.array([[1,2,34,4,5,6], [2,2,94,45,56,7]])
# print(arr)
# # Create an array with 5 dimensions using ndmin using a vector with values 
# # 1,2,3,4 and verify that last dimension has value 4:
# vec = np.array([1,3,4,5,6], ndmin=5)
# print(vec)
# print("Shape of the array is: ", vec.shape)

# 1D to 2D:
# third = np.array([1,2,3,4,5,6,7,8])
# newarr = third.reshape(4, 2)
# print(newarr)

# # #1D to 3D:
# four = np.array([1,2,3,45,6,7,8,9,23,4,3,87,32,45,3,])
# newfour = four.reshape(1,5,3)
# newarr
# print(newfour)
# # 3D to 1D:
# arrr = np.array([[[1,2,4,7], [2,34,45,5]], [[1,3,45,5], [1,23,32,12]]])
# newarrr = arrr.reshape(-1)
# print(newarrr)
# # joining two arrays:
# new = np.array([1,23,4,5])
# new1= np.array([7,8,9,23,4])
# new2 = np.concatenate((new, new1))
# print(new2)
# # joining 3arrays:
# new = np.array([1,23,4,5])
# new1= np.array([7,8,9,23,4])
# new2 = np.array([21,22,32,45])
# ew2 = np.concatenate((new, new1, new2))
# print(ew2)
# #joining two array along with rows:
# new = np.array([1,23,4,5])
# new1= np.array([7,8,9,23,4])
# new2 = np.hstack((new, new1))
# print(new2)

# new = np.array([1,23,4,5,7,8,9,23,4])
# new1 = np.array_split(new, 3)
# print(new1)
# print(new1[0])

# np searching:
# lear = np.array([1,23,3,3,4,56,6,3,5,3])
# c = np.where(lear %2==0)
# print(c)
# learr = np.array([1,23,3,3,4,56,6,3,5,3])
# d = np.searchsorted(learr, 4, side='right')
# print(d)

# array sorting:
# f = np.array([2,4,5,7,2,3])
# g = np.sort(f)
# print(g)
# h = np.array(["bana", "cherry", "apple", "sugar", "drop"])
# print(np.sort(h))

# filtering array:
# arr = np.array([1,2,34,56,3,5])
# fil_arr = []
# for element in arr:
#     if element > 5:
#         fil_arr.append(True)
#     else:
#         fil_arr.append(False)

# narr = arr[fil_arr]
# print(fil_arr)
# # print(narr)
# evenn = np.array([1,2,4,5,8,34,22,7])
# narr = []
# for element in evenn:
#     if element % 2 == 0:
#         narr.append(True)
#     else:
#         narr.append(False)
# neven = evenn[narr]
# print(neven)
# print(narr)
#we can also do like this:
# odd  = np.array([1,34,23,45,23,22])
# nood = odd % 2==1
# nnodd = odd[nood]
# print(nood)
# print(nnodd)

# creating random no:
# y = random.randint((100), size = (3))
# print(y)
# x = random.choice([3,4,6,7], p=[0.1, 0.2, 0.3,0.4], size=())
# print(x)
# y = random.choice([2,3,4], p=[0.3,0.3,0.4], size=())
# print(y)
# randompass = random.choice([3,4,6,7], p=[0.1, 0.2, 0.3,0.4], size=(5))
# print(randompass)

# vectorization ml topic:
# w  = np.array([1,2,4,6,8,9])
# b = 3
# x = np.array([2.0, 2.1, 3.1,1.2, 0.3, 1.2])

# f = np.dot(w, x) + b
# print(f)
# random_num = np.random.uniform(2, 10, 3)
# print(random_num)