'''
捕获所有异常
'''
try:
    #print(8/0)
    f = open('python.txt','r')
except Exception as e:
    print(e)

