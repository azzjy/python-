class Animal(object):
    def run(self):
        print('Animal is running')

class Dog(Animal):
    def run(self):
        print('dog is running')

class Cat(Animal):
    def run(self):
        print('cat is running')


d = Dog()
d.run()
c = Cat()
c.run()

a = Animal()
a.run()
print(isinstance(d,Dog))

print(isinstance(a,Dog))

'''
多态
对于一个变量，我们只需要知道它是Animal类型，
无需确切地知道它的子类型，就可以放心地调用run()方法，
而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，
由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，
而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。
这就是著名的“开闭”原则：
'''
def run_twice(a):
    a.run()
    a.run()

run_twice(Dog())

run_twice(Cat())

print(type(a))
print(type(abs))