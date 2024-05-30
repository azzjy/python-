'''
os.mkdir(新文件夹名)
os.getcwd() 获取当前目录名称
os.chdir(切换后目录名称) 切换目录
os.listdit(目标目录) 获取指定目录下的文件信息，返回列表
os.rmdir(目标目录) 用于删除一个指定名称的'空'文件夹
'''

import os

#判断文件夹是否存在
if not os.path.exists('./文件操作/os模块/images'):
    os.mkdir('./文件操作/os模块/images')

#获取当前目录
print(os.getcwd())

#切换目录
#os.chdir('')
#列出当前目录下的所有文件
print(os.listdir())


