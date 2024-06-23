import time
def get_time(fn):

    def inner():
        start = time.time()
        fn()
        end = time.time()
        print(f'{fn}函数一共执行花费了{end-start}s')
    return inner




@get_time
def func():
    list1 = []
    for i in range(10000000):
        list1.append(i)

func()