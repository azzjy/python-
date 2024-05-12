'''
len() 求数据的长度 len(数据对象)
del 列表[下标或者key]
'''

str1 = "abcdef"
print(len(str1))


list1 = [1,2,3,4,5]

print(len(list1))

dict1 = {"name":"章三","age":17,"phone":"17712345987"}

print(len(dict1))

# del

del list1[2]
print(list1)

del dict1['age']

print(dict1)



