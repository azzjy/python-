'''
max()返回序列中的最大值
min() 返回序列中的最小值
案例： 输入3个数字，求三个数中的最大值与最小值
'''

num1 = int(input('请输入第一个数:'))

num2 = int(input('请输入第二个数:'))

num3 = int(input('请输入第三个数:'))

# 下划线也是变量组成字符之一
max_ = max(num1,num2,num3)
print(max_)

# 最小值

min_ = min(num1,num2,num3)

print(min_)