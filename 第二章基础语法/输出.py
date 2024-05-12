age = 18
name = 'TOM'
weight = 75.5
stu_id = 1

stu_id2 = 1000

print('我的年龄是%d岁' %age)

print('我的名字是%s' %name)

print('我的体重是%.2f公斤' %weight)

print('我的学号是%06d' %stu_id)

print('我的学号:%03d' %stu_id2)

print('我的名字是%s,今年%d岁,明年%d岁了,体重是%.2f,学号是%06d' %(name,age,age,weight,stu_id))

print('我的名字是%s,今年%s岁了,体重%s公斤' %(name,age,weight))


print(f'我的名字是{name},今年{age}岁了,体重是{weight}') #高效输出 f格式话是3.6以上才可以用


