#导入 os模块
import os

import time

os.rename('./文件操作/os模块/python.txt','./文件操作/os模块/linux.txt')

time.sleep(20)

print('更名成功！')

os.remove('./文件操作/os模块/linux.txt')