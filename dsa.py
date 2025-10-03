# my_array = [25,45,76,23,44]
# min_val = my_array[0]
# for i in my_array:
#     if i < min_val:
#         min_val = i
# print("min value in this array is: ", min_val)

# pre1 = 0
# pre2 = 1
# # print(pre1)
# # print(pre2)
# for fibo in range(9):
#     newpre = pre1 + pre2
#     print(newpre)
#     pre1 = pre2
#     pre2 = newpre

# m_array = [1,5,6,7,8,9,2,3,4,10]
# n = len(m_array)
# for i in range(n-1):
#     min_index = i
#     for j in range(i + 1, n):
#         if m_array[j] < m_array[min_index]:
#             min_index = j
#     min_value = m_array.pop(min_index)
#     m_array.insert(i, min_value)
# print(m_array)
# array = [34,45,3,23,45,76,78,23]
# n = len(array)
# for i in range(n-1):
#     min_index = i
#     for j in range(i + 1, n):
#         if array[j] < array[min_index]:
#             min_index = j
#     min_value = array.pop(min_index)
#     array.insert(i, min_value)
#     print(array)

array = [78,43,46,32,57,327,98,67,243]
n = len(array)
for i in range(n - 1):
    minindex = i
    for j in range(i +1, n):
        if array[j] < array[minindex]:
            minindex = j
    minval = array.pop(minindex)
    array.insert(i, minval) 
print(array)