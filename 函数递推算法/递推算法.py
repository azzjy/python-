'''
使用递推算法求斐波那契数列
斐波那契数列：1 1 2 3 5 8 13 21 34
'''
#n 代表斐波那契数列的第n位的结果
def func(n):
    if n == 1 or n == 2:
        return 1
    dict1 = {1:1,2:1}
    #从第三位开始其结果等于前两位之和
    for i in range(3,n+1):
        dict1[i] = dict1[i-1] + dict1[i-2]
    return dict1[n]

print(func(15))
