class Student(object):
    def __init__(self,name,gender):
        self.__name = name
        self.__gender = gender

    def get_gender(self):
        print(self.__gender)
    def set_gender(self,gender):
        self.__gender = gender
s1 = Student('Lisa',89);
s1.get_gender()
s1.set_gender(100)
s1.get_gender()