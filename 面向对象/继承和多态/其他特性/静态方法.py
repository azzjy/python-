'''
在开发时，如果需要在类中封装一个方法，这方法
    1. 既不需要访问实例属性或者调用实例方法
    2. 也不需要访问类属性或调用类方法
静态方法
class Game(object):
    @staticmethod
    def menu():
        print('11')

调用
Game.menu()
'''


class Game(object):
    @staticmethod
    def menu():
        print('11')


Game.menu()
#实例化对象
game = Game()
game.menu()