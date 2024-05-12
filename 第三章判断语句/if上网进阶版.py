input_age = input("请输入您的年龄:")
age = eval(input_age)
if age >= 18:
    print(f'您的年龄为{age},可以上网了，请上网')
else:
    print('未成年不得上网！')
print('程序退出')