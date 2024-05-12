'''
global全局关键字

我们知道python中的变量分为两种形式，
    1. 全局变量（全局范围）
    2. 局部变量（局部范围）
我们能不能在局部作用域中对全局变量进行修改
'''

num = 10

def func():
    #声明变量num，代表接下来我要使用的num都是全局中的num变量
    global num
    # 局部变量没办法修改全局变量的值
    num = 100
    #print(num)
func()
print(num)


