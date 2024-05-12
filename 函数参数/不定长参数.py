'''
不定长参数也叫可变参数。用于不确定调用的时候会传递多少个参数（不传参数也可以）
不定长元祖参数，我们可以通过*args对其进行接受，其返回参数args是一个元祖
'''

#不定长元祖参数
def user_info(*args):
    print(args)
    print(type(args))

user_info("ROSE",19,'female')
user_info('Lucy',19)
