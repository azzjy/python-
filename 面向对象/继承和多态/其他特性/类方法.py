'''
类是一个抽象 => 在python中一切皆对象
类理解为是一个特殊的对象 => 类属性和类方法

类方法就是针对类对象定义的方法，在类方法中可以直接访问类属性或者调用其他类方法
    1. 访问和操纵类属性
    2. 调用其他的类方法
定义
@classmethod
def 类方法名称(cls):
    pass

    1. 有哪一个类调用的方法，方法内的'cls'就是那一个类的引用
    2. 这个参数和示例方法的第一个参数是'self'类似
    3. 提示使用其他名称也可以，不过习惯使用‘cls’通过类名.调用类方法，调用方法时，不需要传递'cls'参数

在方法内部:
    1. 可以通过'cls.'访问类的属性
    2. 也可以通过'cls.'调用其他类方法
'''


class Tool(object):
    count = 0

    def __init__(self,name):
        self.name = name
        Tool.count += 1

    @classmethod
    def show_tools_count(cls):
        print(f'当前{cls}类一共被实例化{cls.count}次')
    

t1 = Tool('剪子')

t2 = Tool('榔头')


print(Tool.show_tools_count())