
students = []


def funcA():
    global students
    students.append(1)
    students.append(2)
    students.append(3)
def funcB():
    for i in students:
        print(i)
#添加数据
funcA()
#读取数据
funcB()