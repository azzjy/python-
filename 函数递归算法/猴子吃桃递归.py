def peaches(n):
    if n == 1:
        return 1
    else:
        return 2 * (peaches(n - 1) + 1)

# 测试
print(peaches(5))