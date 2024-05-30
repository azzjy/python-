'''
    异常捕获 
    try:
        可能出问题的代码段
    except:
        出问题后怎么解决，提示还是怎么样
'''

try:
    f = open('python.txt','r')
    print(f.read())
except IOError:
    print('没有找到文件或读取文件失败！')
else:
    f.close()


print('你好世界')