'''
*args不定长元祖参数
'''
fn1 = lambda *args: args

#不定长字典
fn2 = lambda **kwargs: kwargs

print(fn1(1,2,3,6))

print(fn2(name='Tom',age=16,address='深圳宝安'))