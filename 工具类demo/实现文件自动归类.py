import shutil
import os
path = "/Users/zoujunping/Desktop/视频"
files = os.listdir(path)
for f in files:
    end = f.split(".")[-1]
    if not os.path.exists(path + "/"+end):
        os.makedirs(path + "/"+end)
    shutil.move(path+"/"+f, path + "/"+end)
#目的: 把一批文件,按照后缀名新建对应的文件夹,并移动相应的文件到对应的文件夹.实现文件的自动归类.
# 1.比如一个文件里有很多不同类型的文件，图片，视频，需求图
# 2 然后这个代码run后会自动创建不用的文件夹，文件夹下会有同类型的文件
# 比如 jpeg下面全是jpeg格式的图片文件
# 比如 视频下面全是mp4格式的视频文件
# 比如 sketch下面全是sketch格式的sketch文件