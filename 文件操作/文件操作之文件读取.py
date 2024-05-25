f = open('./文件操作/python.txt','r',encoding='utf-8')

content = f.read(1024)

print(content)

f.close()