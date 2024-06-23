#定义一个装饰器
#参数fn，要求传递要修饰函数的名称
# 1. 有嵌套
def check(fn):
    def inner():
        #编写装饰器功能
        print('请先登录')
        # 2. 有引用
        fn()
    # 3. 有返回  返回的是内存地址
    return inner


def comment():
    print('编写评论')


#调用装饰器代码装饰comment函数

comment = check(comment)
comment() #由于comment指向了inner函数，所以comment()代表执行了inner函数