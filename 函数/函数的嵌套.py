'''
函数的嵌套
函数嵌套时函数的执行步骤
'''

def funcB():
    print('这是函数funcB的函数体部分')


def funcA():
    print('-'*40)
    print('这是函数funcA的函数体部分')
    funcB()
    print('-'*40)


funcA()