'''
修改
'''
mystr = 'hello world and itcast and itheima and python'

# replace有返回值是修改后的字符串，不会改变原有字符串
# 说明字符串是不可变数据类型


# 数据是否可以改变划分为 可变类型 和 不可变类型

# 替换次数如果超出子串出现的次数 表示替换所有这个子串

new_str = mystr.replace('and','和',5)

print(new_str)

## split() --- 分割 返回一个列表 丢失分割字符

new_str1 = mystr.split('and')

print(new_str1)


# join 合并列表里面的数据为一个大字符串

mylist = ['aa','bb','cc']

mm = '...'.join(mylist)

print(mm)