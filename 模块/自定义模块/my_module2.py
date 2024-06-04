# 1. 定义两个数的加和
def add_num(num1,num2):
    return num1+num2


# 2. 定义两个数的相减
def sub_num(num1,num2):
    return num1-num2



#魔术变量 _ _name_ _

#print(__name__) #返回__main__ 当前文件运行结果

#在当前文件中之际调用相关功能进行测试 下面是测试代码
if __name__ == '__main__':
    print(add_num(10,22))