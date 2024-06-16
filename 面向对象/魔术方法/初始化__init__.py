'''
初始化方法或构造方法

__init__()

为对象赋予相关属性

执行过程；
    当这个类被实例化时，则__init__()方法会被系统调用

'''

class Person(object):

    def __init__(self,name,age):
        self.name = name
        self.age = age


p1 = Person('章三',13)


p2 = Person()

p2.age = 13

print(p2.age)
