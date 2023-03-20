import os
import random
import re
from time import sleep

from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent
from lxml import etree

def photoxiaoshuo(number):
    # 随机usera-gent，防止被封
    ua = UserAgent()
    head = ua.chrome
    header = {
        "user-agent": head
    }
    url = 'https://m.xbiquge.so/list/1_'+str(number)+'.html'
    response = requests.get(url, headers=header)
    xml = BeautifulSoup(response.text, 'lxml')
    html = etree.HTML(response.text)
    name = html.xpath("//div[@class='article']/a[1]/text()")
    #用xpath来定位有点问题，只能使用BeautifulSoup库
    imgall = xml.find_all('img')
    img = []
    for i in imgall:
        img.append(i['src'])
    bookname = '小说玄幻图片'
    if not os.path.exists(bookname):
        os.mkdir(bookname)
    for i, a in zip(name, img):
        imgs = i + '.jpg'
        #随机时间防止ip被封
        sleep(random.uniform(0, 2))
        reponse1 = requests.get(a).content
        with open(bookname + '/' + imgs, 'wb') as f:
            f.write(reponse1)
        print('正在下载小说图片:' + i + '')
#自定义爬取页面数,目前爬取一页只做示范
for i in range(1,2):
    photoxiaoshuo(i)
    print('------------------------第'+str(i)+'页下载完成------------------------')
