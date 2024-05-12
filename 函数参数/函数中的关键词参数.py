'''
关键词参数

通过 键=值
'''

def user_info(name,age,address):
    print(name)
    print(age)
    print(address)

#对参数位置没有要求  关键字参数
user_info(age=20,name='asd',address='asads')