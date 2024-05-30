def menu():
    print('-' * 40)
    print('学生管理系统V1.0')
    print('[1]添加学生信息')
    print('[2]删除学生信息')
    print('[3]修改学生信息')
    print('[4]查询学生信息')
    print('[5]遍历所有学生信息')
    print('[6]保存数据到文件')
    print('[7]退出系统')
    print('-' * 40)

students = []
def add_student():
    global students
    student = {}
    name = input('请输入学生姓名:')
    age = int(input('请输入学生年龄:'))
    phone = input('请输入学生手机号：')
    student['name'] = name
    student['age'] = age
    student['phone'] = phone
    students.append(student)
    print(f'添加{name}学生信息成功')
def del_student():
    global students
    name = input('请输入要删除的学生姓名:')
    for i in students:
        if i['name'] == name:
            students.remove(i)
            print(f'学生信息{name}删除成功')
            break
    else:
        print('抱歉没找到要删除的人,请重新输入！')

def select_student_all():
    global students
    for i in students:
        print(i)


def update_student():
    global students
    name = input('请输入要修改的学生姓名:')
    for i in students:
        if i['name'] == name:
            new_name = input('请输入新的姓名:')
            new_age = int(input('请输入年龄：'))
            new_phone = input('请输入手机号：')
            i['name'] = new_name
            i['age'] = new_age
            i['phone'] = new_phone
            print(f'学生信息{new_name}更新成功')
            break
    else:
        print('抱歉没找到要更新的人,请重新输入！')

def get_student():
    global students
    name = input('请输入要查询学生的姓名:')
    for i in students:
        if i['name'] == name:
            print(i)
            break
    else:
        print('抱歉没有找到')
def save_data_to_file():
    global students
    #判断数据是否为空，为空不保存
    if len(students) == 0:
        return
    f = open('./data.txt','w',encoding='utf-8')
    f.write(str(students))
    f.close()

#初始化学生信息
def init_student():
    global students
    f = open('./data.txt','r',encoding='utf-8')
    content = f.read(1024)
    students = eval(content)
    f.close()

init_student()
while True:
    menu()
    user_num = int(input('请输入您要操作的编号:'))
    if 1 == user_num:
        add_student()
    elif 2 == user_num:
        del_student()
    elif 3 == user_num:
        update_student()
    elif 4 == user_num:
        get_student()
    elif 5 == user_num:
        select_student_all()
    elif 6 == user_num:
        save_data_to_file()
    elif 7 == user_num:
        break
    else:
        print('您输入的功能编号错误，请重新输入！')

