def outer():
    num = 10
    def inner():
        #global num   #global不起作用
        nonlocal num  #只能声明局部变量
        num = 20
        #print(f'inner函数中的num变量值:{num}')
    print(f'outer函数中的num变量值:{num}')
    inner()
    print(f'当inner函数执行完毕后,查看outer函数中的num是否有影响{num}')


outer()

#print(num)