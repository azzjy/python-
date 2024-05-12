'''
数据类型转换
'''

num1 = 1
str1 = 10

print(type(float(num1)))


list1 = [10,20,30]

print(tuple(list1))

t1 = (100,200,300)

print(list(t1))


#eval()

str2 = '1'

str3 = '1.1'

str4 = '(1000,2000,3000)'

str5 = '[1000,2000,3000]'

str6 = "{'name':'章三'}"

str7 = "{2,3,4,5}"

print(type(eval(str2)))

print(type(eval(str3)))

print(type(eval(str4)))

print(type(eval(str5)))

print(type(eval(str6)))

print(type(eval(str7)))