'''
__str__()
在编写__str__()魔术方法时，其返回结果必须是一个字符串类型的数据，否则会报错
'''

class Car(object):
    #在一个类中，自身的属性都是通用的，可以相互访问
    def __init__(self,color,plate):
        self.color = color
        self.plate = plate
    #当print(对象)时，__str__()魔术方法会自动被触发(被调用)
    def __str__(self):
        #要求：必须有return返回值，且返回的数据类型必须是一个字符串类型
        return f'颜色:{self.color},车牌{self.plate}'
c1 = Car('黄色','沪A77711')

print(c1)