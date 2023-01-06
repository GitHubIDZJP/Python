import os
# path = '/Users/zoujunping/Desktop/资源'

# !/usr/bin/python
# -*- coding:utf8 -*-

import os
import sys


def cur_file_dir():
    # 获取当前文件路径
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def ReName(filpath):
    video_list = os.listdir(filpath)
    for video_index in range(0, len(video_list)):
        full_name = os.path.join(filpath, video_list[video_index])
        video_name = video_list[video_index]
        if video_name[0].isdigit():
            file_extension = video_name.split(".")[-1]
            video_name = video_name.split(".")[0]
            video_names = video_name.split('-', 1)
            digit = video_names[0]
            real_name = video_names[1]
            rename = real_name + "-" + digit + "." + file_extension
            os.rename(full_name, os.path.join(filpath, rename))


if __name__ == '__main__':
    filepath = r'/Users/zoujunping/Desktop/资源'
    ReName(filepath)

