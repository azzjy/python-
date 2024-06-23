def check(fn):
    def inner():
        print('请先登录')
        fn()
    return inner

@check
def comment():
    print('编写评论')


comment()


#@classmethod
#@staticmethod