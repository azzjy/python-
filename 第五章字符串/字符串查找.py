'''
字符串查找
'''


mystr = "hello world and itcast and itheima and python"

print(mystr.find('and'))

print(mystr.find('ands',15,30))

# index
print(mystr.index('and'))
print(mystr.index('and',15,30))

# count()

print(mystr.count('and',15,30)) #1

print(mystr.count('and')) # 3

print(mystr.count('ands'))


# rfind

print(mystr.rfind('and'))

print(mystr.rindex('and'))

##### 视频看到4----字符串，04常用操作方法之查找已经看完，往后看05