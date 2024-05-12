'''
序列类型相互转换
'''
tuple1 = (10,20,30)

print(list(tuple1))

# 字典转列表只能把key作为列表的元素， value会自动舍弃
dict1 = {'name':'TOM','age':23,'address':'深圳市宝安区'}

print(list(dict1))


# tuple() 转换为元祖
list1 = [10]
print(tuple(list1))

set1 = {10,20,30,40,50}
print(tuple(set1))


# set()转为集合

list2 = [10,20,30,20,40]

print(set(list2).sort())