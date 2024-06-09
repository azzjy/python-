class Cat(object):
    #定义相关属性和方法
    def eat(self):
        print('喜欢吃猫粮')
    def drink(self):
        print('喝纯净水')


c1 = Cat()

#属性
c1.name = 'Tom'
c1.color = '橘黄色'
print(c1.name)
print(c1.color)
