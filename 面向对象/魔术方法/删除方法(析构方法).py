'''
__del__() 当删除对象时(调用del删除对象或文件执行结束后)，python解释器也会默认调用__del__()方法
'''

class Person(object):
    def __init__(self,name,age):
            self.name = name
            self.age = age
    
    '''
    当对象执行完毕时执行
    '''
    def __del__(self):
          print('对象被删除或销毁时，自动被调用')


p1 = Person('张三',19)

