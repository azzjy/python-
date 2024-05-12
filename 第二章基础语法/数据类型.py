"""
 1. 按照经验将不同的变量存储不同的类型的数据
 2. 验证这些数据到底是什么类型--检测数据类型 --type(数据)
"""

name1 = 1 #int 整数
name2 = 1.1 # float 浮点型

print(type(name1))
print(type(name2))

flag = False
flag1 = True
print(type(flag))
print(type(flag1))

# str --- 字符串
a = "Hello World"
print(type(a))

# list --- 列表
alist = [1,3,4,5,'qwe']
print(type(alist))

# tuple -- 元组
d = (10,20,30)
print(type(d))

# set --- 集合
e = {10,20,40}
print(type(e))

# dist --- 字典
f = {'name':'章三','age':12}
print(type(f))