'''
raise抛出自定义异常
语法 raise 异常类对象
'''

def input_password():
    pass_word = input('请输入您的密码(要求密码长度不能低于6位):')
    if len(pass_word) < 6:
        raise Exception('您输入的密码长度小于6位')
        #print('您输入的密码长度小于6位')

input_password()