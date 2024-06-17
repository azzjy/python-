'''
多态特性:一种公共方法，随着传入的参数(对象)不同，则同一个方法可以返回不同的结果
'''
class Fruit(object):
    def makejuice(self):
        print('i can make juice')

class Apple(Fruit):
    def makejuice(self):
        print('i can make Apple juice')

class Banana(Fruit):
    def makejuice(self):
        print('i can make Banana juice')

#定义公共的方法用于调用makejuice功能

def service(obj):
    obj.makejuice()


fru = Fruit()
service(fru)

apple = Apple()

service(apple)

banana = Banana()

service(banana)