def func(*args,**kwagrs):
    #既能接受元祖类型的数据，也可以接受字典类型的数据
    result = 0
    for i in args:
        result += i
    
    for i in kwagrs.values():
        result += i
    return result


print(func(10,20,30,num1=40,num2=50))



# 定义一个函数，使用args/kwargs接收不定长参数
def funcA(*args,**kwagrs):
    print(args)
    print(kwagrs)

#先定义变量，再传递值

tuple1 = (10,20,30)

dict1 = {'num1':40,'num2':50,'num3':60}

#funcA(tuple1,dict1)
funcA(*tuple1,**dict1)

