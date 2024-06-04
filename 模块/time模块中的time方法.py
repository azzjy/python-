from time import time as t

#time.time() 获取当前系统时间

start = t()
list1 = []

for u in range(100000):
    list1.append(u)

end = t()

print(f'您的程序一共执行花费了{end-start:.2f}s时间')