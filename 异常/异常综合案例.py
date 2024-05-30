'''
1.尝试只读方式打开python.txt文件，如果文件存在则读取文件内容，如果文件不存在则提示用户即可
2.读取内容要求:尝试循环读取内容，读取过程中如果检测到用户终止程序，则except捕获
'''
try:
    f = open('python.txt','r')

except:
    print('访问的python,txt文件不存在！')