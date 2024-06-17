class Person(object):
    #类属性
    count = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        # self.name和self.age中的name/age属性就是实例属性(对象属性)
        #类名.属性，相当于调用类属性
        Person.count += 1


p1 = Person('Tom',23)

p2 = Person('Lily',19)

print(f'Person类一共实例化了{Person.count}次')