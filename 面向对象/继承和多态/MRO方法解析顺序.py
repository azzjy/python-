'''
MRO(Method Resolution Order):方法解析顺序，我们可以通过类名.__mor__或类名.mro()获得‘类的层次结构’，方法解析顺序也是按照这个类的层次结构寻找到
'''
class Car(object):
    def __init__(self,brand,color,model):
        self.brand = brand
        self.color = color
        self.model = model
    
    def run(self):
        print('i can run')

class GasonlineCar(Car):
    pass

class EletricCar(Car):
    def __init__(self, brand, color, model,battery):
        #强制调用父类中的__init__()初始化方法，用于实现对brand/color/model属性进行初始化
        super().__init__(brand, color, model)
        self.battery = battery

    def run(self):
        print('i can run eletric')
    
tesla = EletricCar('Tesla','粉色','Model S',70)


print(tesla.brand)

print(tesla.color)

print(tesla.model)

tesla.run()

print(EletricCar.__mro__)
print(EletricCar.mro())