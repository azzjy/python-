list1 = [10,20,15,30,25]

#升序
list1.sort()

print(list1)

#倒序
list1.reverse()

print(list1)



studets =[
    {'name':'Tom','age':20},
    {'name':'Rose','age':19},
    {'name':'Jack','age':22}
]

#按照 name a-z或A-Z
#studets.sort()
print(studets)

#sort(key=元素按照元素的key排序)
#sort(key=必须是一个函数)，实际工作中，key=经常与lambda表达式结合
#按照升序排列
studets.sort(key=lambda x:x['name'])
#studes本身是一个列表其内部是由三个字典组成的
#当我们使用students.sort()，系统首先会将列表中的3个字典元素通过遍历的方式循环取出
#当我们第一次循环时，系统会将第一个字典取出来，然后放入变量X中，经过lambda表示式返回结果x['name'] = Tom
print(studets)


#使用lambda表示对其降序排列

studets.sort(key=lambda x:x['name'],reverse=True)
print(studets)