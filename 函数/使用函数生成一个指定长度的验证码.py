'''
生成一个指定长度的验证码，验证码的每个元素都是随机的
'''
import random
def generate_code(num):
    '''
    generate_code函数主要用于生成指定长度的字符，字符是随机的
    :param num: 代表生成发验证码的长度
    :return: 返回num长度的随机验证码
    '''
    str1 = '123456789abcdefghjkmnpqrstuvwxyzABCDEFGHGKMNPQRSTUVWXYZ'
    code = ''
    for i in range(num):
        code+=str1[random.randint(0,len(str1)-1)]
    
    return code

# 调用generate_code函数
print(generate_code(6))

help(generate_code)