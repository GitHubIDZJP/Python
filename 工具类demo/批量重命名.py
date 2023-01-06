import shutil
import os
path = "/Users/zoujunping/Desktop/imgs"
files = os.listdir(path)
fn_path = os.getcwd() #获取当前工作目录
fn = os.listdir(path)#返回工作目录中的所有文件和子目录
# 通过.getcwd()和.listdir(path)这两个函数，我们就获取了当前工作目录下的所有文件。
print(fn) #打印文件目录

file_mp4= [i for i in files if i.split(".")[-1] == "mp4"]
print('筛选文件类型:',file_mp4) #输出图片jpeg

#把截图无序的命名，放进imgs文件夹里，然后run下面代码，效果就是给图片命名会1,2 3,4,5,6,7,8,9.后缀格式(自定义) 到末尾
i = 0
filelist = os.listdir(path)
#该文件夹下所有的文件（包括文件夹）
for files in filelist:   #遍历所有文件
    i = i + 1
    Olddir = os.path.join(path, files)    #原来的文件路径
    if os.path.isdir(Olddir):       #如果是文件夹则跳过
            continue
    filetype = '.png'        #文件扩展名
    Newdir = os.path.join(path, str(i) + filetype)   #新的文件路径
    os.rename(Olddir, Newdir)
    print(Olddir)
    print(Newdir)



