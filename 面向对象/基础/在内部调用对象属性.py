class monkey(object):
    def show_info(self):
        print(f'我的名字叫:{self.name},我的金呢个:{self.skill}')


sun = monkey()

sun.name = 'sun'

sun.skill = '筋斗云'

sun.show_info()