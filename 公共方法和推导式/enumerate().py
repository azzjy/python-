'''
 enumerate() 把序列类型的数据构造成key：value 结构，然后结合for循环进行遍历    包括 列表 元祖 字符串
'''


str1 = "abcdrfg"

for i in enumerate(str1):
    print(i)

print('-'*20)
list1 = [10,20,30,40,50]
for key,values in enumerate(list1):
    print(f'{key}======{values}')



dict1 = {'name':'章三','age':19,'phone':'19912344321'}

for key,values in dict1.items():
    print(f'{key}===={values}')


