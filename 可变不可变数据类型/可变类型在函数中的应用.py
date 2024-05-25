'''
可变类型在函数中的应用场景
'''

def func(names):
    names.append('找刘')

names = ['章三','里斯','王五']

func(names)

print(names)