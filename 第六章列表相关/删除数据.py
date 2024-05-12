name_list = ['TOM','Lily','ROSE']

# del 目标  可以指定下标 或者整个删除整个列表
#del name_list[0]
print(name_list)




# pop()  删除置顶下标数据，如果不指定下标 默认删除最后一个数据  无论是按照下标还是删除最后一个   pop函数都会返回这个被删除的数据
#del_list = name_list.pop(1)

#print(name_list)

#print(del_list)

# remove() 删除指定数据

name_list.remove('TOM')
print(name_list)

# clear()
name_list.clear()


print(name_list)




