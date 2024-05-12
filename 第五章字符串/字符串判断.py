'''
是布尔型类型数据
'''

mystr = "hello world and itcast and itheima and Python"

# startswith 字符串.startswith(子串,开始位置下标,结束位置下标) 判断字符串是否以某个子串开头

print(mystr.startswith('hello'))

print(mystr.startswith('hel'))

print(mystr.startswith('hels'))


# endswith   判断字符串是否以某个子串结尾
print(mystr.endswith('Python'))

print(mystr.endswith('Pythons'))


# isalpha() 判断非空字符串  字母


print(mystr.isalpha())

# isdigit()   判断都是数字返回True

print(mystr.isdigit())

mystr1 = '123456'

print(mystr1.isdigit())

# isalnum() 数字或者字母组合

print(mystr.isalnum())

mystr2 = 'abc123'

print(mystr2.isalnum())


# issplce()  都是空格返回True

print(mystr.isspace())

mystr3 = '   '

print(mystr3.isspace())



