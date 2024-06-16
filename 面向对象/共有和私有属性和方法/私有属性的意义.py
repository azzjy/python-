class Person(object):
    def __init__(self,name):
        self.name = name
        self.__salary = 18000
    def set_salary(self,salary):
        #经过权限验证才可以操作
        self.__salary = salary
    def get_salary(self):
        #验证权限
        return self.__salary
p1 = Person('章三')
p1.salary = 28000

print(p1.salary)

p1.set_salary(19999)

print(p1.salary)

print(p1.get_salary())