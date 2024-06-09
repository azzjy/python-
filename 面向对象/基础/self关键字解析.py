class Person(object):
    def eat(self):
        print(self)
        print('吃吃吃')
    def drink(self):
        print('喝喝喝')

#self代表对象本身
p1 = Person()
print(p1)
p1.eat()

p2 = Person()

print(p2)

p2.eat()