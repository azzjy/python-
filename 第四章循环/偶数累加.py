'''
1-100 偶数累加和
'''

i = 1
result = 0

while i <=100:
    if i%2 == 0:
        result+=i
    i+=1
print(result)


'''
优化
'''

a = 2

result1 = 0

while a<=100:
    result1 +=a
    a+=2

print(result1)