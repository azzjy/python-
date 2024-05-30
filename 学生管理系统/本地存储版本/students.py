students = []

student = {}
student['name'] = '章三'
student['age'] = 22
students.append(student)
# f = open('./data.txt','w',encoding='utf-8')
# f.write(str(students))
# f.close()

f = open('./data.txt','r',encoding='utf-8')
content = f.read(1024)
print(content)

#把字符串转换为原数据类型
content = eval(content)
print(content)
print(type(content))
f.close()
