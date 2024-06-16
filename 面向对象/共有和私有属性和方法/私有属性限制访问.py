'''
在属性名和方法名前面加两个下划线__即可。
'''
'''
访问私有属性使用get_xx来获取私有属性，定义set__xx用来修改私有属性值。
外部用过特定的'接口'来实现对私有属性的方法
'''
class Girl(object):
    def __init__(self,name):
        self.name = name
        self.__age = 18
    '''
    这个函数并不是对所有的用户开放，只会针对特定的用户(角色验证)
    '''
    def get_salary():
        pass

xiaomei = Girl('xiaomei')

print(xiaomei.name)
print(xiaomei.__age)





