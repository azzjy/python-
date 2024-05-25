'''
一个正整数的阶乘是所有小于及等于该数的正整数的积，如： n!=1x2x3x....x(n-1)xn
'''


def func(num):
    if num <= 2:
        return num
    return num * func(num-1)

print(func(10))