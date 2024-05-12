'''
缺省参数也叫默认参数，用于定义函数，为参数提供默认值
调用时可传可不传
默认值参数必须放在所有参数的最右边
'''
def user_info(name,age=22,gender='male'):#缺省参数或者默认值参数
    print(name)
    print(age)
    print(gender)

user_info('chen')
user_info('苗青',22,'female')