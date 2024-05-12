'''
字符串对齐
'''

my_str = 'hello'

# 左对齐
new_str = my_str.ljust(10,'.')
print(new_str)


# 右对齐
rnew_str = my_str.rjust(10,'.')

print(rnew_str)

# 中间对齐

cnew_str = my_str.center(11,'s')

print(cnew_str)




