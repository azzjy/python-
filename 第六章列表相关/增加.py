# 列表增加 append()    列表是可变数据类型
# 追加数据的时候如果是一个序列，追加整个序列到列表

name_list = ['TOM','Lily','ROSE']

#name_list.append(['11','22'])

#print(name_list)



# extend() 列表结尾追加数据， 如果数据是一个列表，则将这个序列的数据逐一添加到列表

#name_list.extend('xiaoming')

#name_list.extend(['xiaoming','xiaohong'])

#print(name_list)



# insert() 执行位置新增数据

name_list.insert(1,'xiaoming')

print(name_list)
