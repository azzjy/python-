'''
私有化方法也是通过__方法名()
 不能通过对象直接调用，可以通过对象里面的公共方法，公共方法中调用私有方法
'''
class ATM(object):
    def __func1(self):
        print('插卡')
    def __func2(self):
        print('用户验证')
    def __func3(self):
        print('输入取款金额')
    def __func4(self):
        print('取款')
    def __func5(self):
        print('输出账单')

    #定义公共方法withdraw()专门用于实现取款整个操作
    def withdraw(self):
        self.__func1()
        self.__func2()
        self.__func3()
        self.__func4()
        self.__func5()


atm = ATM()
atm.withdraw()