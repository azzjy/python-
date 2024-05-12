'''
多重判断
'''
age = int(input("请输入您的年龄:"))
#童工
if age < 18:
    print(f'您的年龄为{age}，还未成年，雇佣童工！')
#合法年龄
elif (age >= 18) and (age <= 60):
    print(f'您的年龄为{age}可以打工来')
#退休年龄
else:
    print(f'您的年龄为{age},为退休年龄')
