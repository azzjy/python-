f = open('./文件操作/python.txt','r',encoding='utf-8')


print(f.readlines())#这样写循环无法打印，因为readlines指针已经到最后了
f.seek(0)
for i in f.readlines():
    print(i)

f.close()