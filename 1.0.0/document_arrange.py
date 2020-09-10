import os
from shutil import copyfile
 
def create():
    print('------创建文件夹------')
    for i in var_list:
        Path_now = os.path.join(Path, i).replace('\\', '/')
        if(not os.path.exists(Path_now)):
            os.mkdir(Path_now)
    print('------创建完成------')
 
def move():
    print('------移动文件------')
    for file in os.listdir(Path):
        Path_src = os.path.join(Path, file).replace('\\', '/')
        if(os.path.isfile(Path_src)):
            pos = file.find('.') + 1
            postfix = file[pos:]
            if(postfix in var_list):
                Path_tar = os.path.join(Path, postfix, file).replace('\\', '/')
                copyfile(Path_src, Path_tar)
                os.remove(Path_src)
    print('------移动完成------')
 
var_list = ['jpg', 'jpeg', 'png', 'txt', 'webp', 'gif', 'avi'] #改这里面的内容可以添加整理文件方式(只需要改这里)
Path = input('请输入您要整理的文件夹目录位置： ')
name = input('请输入您要整理的文件夹名称： ')
Path = os.path.join(Path, name).replace('\\', '/')
print(Path)
sure = input('确认您要整理此文件夹吗？ y/n?')
if(sure == 'y'):
    flag = 0
    try:
        flag = os.path.isdir(Path)
    except:
        print('无法打开此文件夹！请确认你具有权限访问此文件夹！！！')
    if(flag):
        print('------开始整理------')
        create()
        move()
    else:
        print('请确认地址指向文件夹')
else:
    print('------exit successfully------')
 
os.system("pause")
