'''
数值和字符串都属于不可变数据类型
'''
a = 10
print(id(a))

b = a
print(id(b))

#尝试更改变量a的值
a = 100
print(id(a))

print(id(b))
print(b)