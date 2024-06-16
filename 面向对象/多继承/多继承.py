'''
汽油车
'''
class GasonlineCar(object):
    def run_with_gasonline(self):
        print('i can run with gasonline')

class EletricCar(object):
    def run_with_eletric(self):
        print('i can run with eletric')


class HybridCar(GasonlineCar,EletricCar):
    pass


bmw = HybridCar()

bmw.run_with_eletric()
bmw.run_with_gasonline()