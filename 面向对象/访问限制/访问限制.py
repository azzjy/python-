'''
如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
'''
class Student(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def show_info(self):
        print(f'姓名:{self.__name}')

s1 = Student('章三',11)

s1.show_info()

print(s1.__age)