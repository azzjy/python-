class Game(object):
    top_score = 0

    def __init__(self,player_name):
        self.player_name = player_name
    
    @staticmethod
    def show_help():
        print('游戏帮助信息')
    
    @classmethod
    def show_top_score(cls):
        print(f'本游戏最高分为:{cls.top_score}')
    
    def start_game(self):
        print('开始游戏')


game = Game('卡卡')

game.show_help()

game.start_game()
