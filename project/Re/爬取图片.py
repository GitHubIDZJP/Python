import requests
import re
import os


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}
name = input('您要爬取什么图片:')
num = 0
x = input('您要爬取几张呢?输入1等于60张图片。:')
name_1 = 'img' #保存图片文件夹
if not os.path.exists(name_1):#判断文件夹是否存在
    os.mkdir(name_1)

    if os.path.getsize(name_1):#判断文件夹是否为空
        for i in os.listdir(name_1):
            os.remove(f'{name_1}{i}')
            for i in range(int(x)):
                url = 'https://image.baidu.com/search/index?tn=baiduimage&word='+name+'&pn='+str(i*30)

                res = requests.get(url,headers=headers)
                htlm_1 = res.content.decode()
                a = re.findall('"objURL":"(.?)",',htlm_1)
                for b in a:
                    num = num +1
                try:
                    img = requests.get(b)
                except Exception as e:
                    print('第'+str(num)+'张图片无法下载------------')
                    print(str(e))
                    # continue
                f = open(name_1+'\image'+str(num)+'.jpg','ab')
                # print(f)
                print('---------正在下载第’+str(num)+‘张图片----------')
                f.write(img.content)
                f.close()
                print(name)
                print('下载完成')
