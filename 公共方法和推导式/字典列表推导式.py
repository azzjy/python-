'''
字典列表推导式
'''

dict1 = {i:i**2 for i in range(1,6)}
print(dict1)

'''
有两个列表
list1 = ['name','age','gender']
list2 = ['Tom',20,'male']

# 结果: person = {'name':'Tom','age':20,'gender':'male'}
'''
list1 = ['name','age','gender']
list2 = ['Tom',20,'male']
dict2 = {list1[i]:list2[i] for i in range(3)}

print(dict2)


