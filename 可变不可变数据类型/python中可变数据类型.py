'''
python中的数据类型
   1. 数值(int整型，float浮点类型)，bool类型(True和Flase)，字符串类型str，元祖(tuple 1,2,3)，列表（list[1,2,3]）,字典（dict{key,value}）,集合（set{1,2,3,4}）
在python中，可以分为两大类，可变类型+非可变类型
 1. 非可变类型
    数值(int整型，float浮点类型)
    bool类型（True,Flase）
    字符串类型(str)
    元祖(tuple 1,2,3)
 2. 可变类型
    列表(list[1,2,3])
    字典(dict{key:value})
    集合(set{1,2})
'''

str1 = 'hello'

print(id(str1))

str2 = str1 + 'world'
print(id(str2))
print(str2)



