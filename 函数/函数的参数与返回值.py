'''
函数的设计原则要遵循高内聚低耦合，尽量要专一，一次完成一个操作
'''

# def geet(name):
#     print(f'您好,{name}')
# geet('老张')
# geet('老李')

def greet(name):
    #当greet函数执行完毕后，其会把返回值返回给函数的调用位置
    return f'{name},你好'


print(greet('老李'))
print(greet('老张'))
