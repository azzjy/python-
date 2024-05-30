'''
else语句和finally

try:
    可以出错的代码
except Exception as e:
    捕获所有异常类型
else:
    表示没有异常要执行的代码
finally:
    无论是否异常都要执行的代码，如文件关闭或者数据库关闭
'''


try:
    f=open('python.txt','r')
except:
    f = open('pyhton.txt','w')
else:
    # 没有遇到异常读取python.txt文件内容
    print(f.read())
finally:
    # 无论是否遇到异常，都要执行finally中的内容
    f.close()

