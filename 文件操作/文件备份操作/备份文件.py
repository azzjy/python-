old_name = input('请输入要备份的文件名称:')

index = old_name.rfind('.')
file_name = old_name[:index]
post_fix = old_name[index:]

#规划备份文件名

new_name = file_name + '[备份]' + post_fix

#把旧文件中的内容拷贝到新文件中已完成备份操作(不仅可以备份文本文件，还可以备份其他文件)
old_f = open(old_name,'rb')
new_f = open(new_name,'wb')

while True:
    content = old_f.read(1024)
    if len(content) == 0:
        break
    new_f.write(content)

old_f.close()
new_f.close()