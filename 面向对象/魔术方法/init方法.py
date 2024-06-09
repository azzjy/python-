'''
以__xxx__() 的函数叫做魔法方法

__init__()初始化方法
'''

class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

p1 = Person('孙悟空',5000)

print(p1.name)
print(p1.age)
