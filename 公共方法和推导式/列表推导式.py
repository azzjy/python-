'''
变量名 = [表达式 for 变量 in 列表]

变量名 = [表达式 for 变量 in 列表 if 条件]

变量名 = [表达式 for 变量 in 列表 for 变量 in 列表]

'''

# list1 = [i for i in range(10)]

# print(list1)


# set1 = {i for i in range(20)}
# print(set1)


# 创建列表推导式，用于简化for循环与if语句

# list1 = [i for i in range(10) if i%2 == 0]
# print(list1)

# 创建列表推导式，用于简化for嵌套循环

# list1 = []

# for i in range(1,3,1):
#     for j in range(0,3,1):
#         a = (i,j)
#         list1.append(a)

# print(list1)


list1 = [(i,j)for i in range(1,3) for j in range(0,3)]
print(list1)