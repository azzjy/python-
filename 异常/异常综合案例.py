'''
1.尝试只读方式打开python.txt文件，如果文件存在则读取文件内容，如果文件不存在则提示用户即可
2.读取内容要求:尝试循环读取内容，读取过程中如果检测到用户终止程序，则except捕获
'''
import time
try:
    f = open('python.txt','r')
    try:
        while True:
            content = f.read(1)
            if len(content) == 0:
                break
            print(content)
            time.sleep(3)
    except:
        print('异常终止代码')
    finally:
        f.close
except:
    print('访问的python,txt文件不存在！')