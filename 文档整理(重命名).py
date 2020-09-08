# coding=utf-8
import os
from shutil import copyfile
from typing import Any

# 全局变量
cnt_jpg = cnt_gif = cnt_png = cnt_txt = cnt_avi = cnt_webp = cnt_pdf = cnt_doc = 0
fileFormat = ['jpg', 'jpeg', 'png', 'txt', 'webp', 'gif', 'avi'] # 分类的文件格式
Path = ""
name = ""
prefix = ""

# 用户输入
def __input():
    global Path, name, prefix
    Path = input('请输入您要整理的文件夹目录位置： ')
    name = input('请输入您要整理的文件夹名称： ')
    prefix = input('请输入重命名后的文件前缀： ')
    Path = os.path.join(Path, name).replace('\\', '/')

# 创建文件夹，如果文件夹中有文件则将这些文件夹移出来
def __create():
    print('------创建文件夹------')
    for i in fileFormat:
        Path_now = os.path.join(Path, i).replace('\\', '/')
        if(not os.path.exists(Path_now)):
            os.mkdir(Path_now)
        else:
            for file in os.listdir(Path_now):
                Path_cur = os.path.join(Path_now, file).replace('\\', '/')
                Path_tar = os.path.join(Path, file).replace('\\', '/')
                copyfile(Path_cur, Path_tar)
                os.remove(Path_cur)
    print('------创建完成------')

# 重命名
def __change(name, var, pos):
    global cnt_jpg, cnt_gif, cnt_png, cnt_txt, cnt_avi, cnt_webp, cnt_doc, cnt_pdf
    if(var == 'jpg'):
        cnt_jpg += 1
        name = name.replace(name[0:pos-1], str(cnt_jpg))
    if(var == 'avi'):
        cnt_avi += 1
        name = name.replace(name[0:pos - 1], str(cnt_avi))
    if(var == 'doc'):
        cnt_doc += 1
        name = name.replace(name[0:pos - 1], str(cnt_doc))
    if(var == 'pdf'):
        cnt_pdf += 1
        name = name.replace(name[0:pos - 1], str(cnt_pdf))
    if(var == 'webp'):
        cnt_webp += 1
        name = name.replace(name[0:pos - 1], str(cnt_webp))
    if(var == 'png'):
        cnt_png += 1
        name = name.replace(name[0:pos-1], str(cnt_png))
    if(var == 'gif'):
        cnt_gif += 1
        name = name.replace(name[0:pos - 1], str(cnt_gif))
    if(var == 'txt'):
        cnt_txt += 1
        name = name.replace(name[0:pos - 1], str(cnt_txt))
    return prefix + name

def __move():
    print('------移动文件------')
    for file in os.listdir(Path):
        Path_src = os.path.join(Path, file).replace('\\', '/')
        if(os.path.isfile(Path_src)):
            pos = file.rfind('.') + 1
            postfix = file[pos:]
            if(postfix in fileFormat):
                file = __change(file, postfix, pos)
                Path_tar = os.path.join(Path, postfix, file).replace('\\', '/')
                copyfile(Path_src, Path_tar)
                os.remove(Path_src)
    print('------移动完成------')

def main():
    __input()
    print(Path)
    sure = input('确认您要整理此文件夹吗？ y/n?')
    if(sure == 'y'):
        if(os.path.isdir(Path)):
            print('------开始整理------')
            __create()
            __move()
        else:
            print('请确认地址指向文件夹，如果确实是文件夹则检查权限问题')
    else:
        print('------exit successfully------')


main()
os.system("pause")