'''
捕获指定异常
'''

try:
    f = open('pyton.txt','r')
except FileNotFoundError:
    print('您要访问的文件不存在!')
