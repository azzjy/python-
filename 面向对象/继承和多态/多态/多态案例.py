class Dog(object):

    #方法体什么都不写是抽象类方法
    def work(self):
        pass

class ArmyDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追查毒品')

class Person(object):
    def work_with_dog(self,dog):
        dog.work()


p = Person()
p.work_with_dog(ArmyDog())
p.work_with_dog(DrugDog())