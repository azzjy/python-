def return_num():
    return (100,200)

print(return_num())

#执行函数，把返回的两个结果，一个放入到变量num1，一个放入变量num2

num1,num2 = return_num()

print(num1)
print(num2)

# 1.如果使用return同时返回多个结果，其返回的数据类型为元祖类型
# 2. 当函数执行完毕