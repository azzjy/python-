'''
try:
    捕获异常体
except (异常1，异常1):

'''

try:
    print(8/0)
    f = open('python.txt','r')
except (FileNotFoundError,ZeroDivisionError):
    #print('除数为0异常')
    print('您要访问的python.txt不存在')