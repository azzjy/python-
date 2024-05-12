name_list = ['TOM','Lily','ROSE']


# in
print('TOM' in name_list)

print('TOMs' in name_list)

# not in
print('TOM' not in name_list)

# 体验判断是否存在

youer_name = input("请输入您的名:")

if youer_name in name_list:
    print(f'您的名字{youer_name}，已经存在不可注册!')
else:
    print(f'您的名字{youer_name}，已经不存在可注册!')




