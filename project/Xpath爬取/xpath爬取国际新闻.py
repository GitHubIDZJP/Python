

#
import os
import parsel
import requests
# 使用 lxml
from lxml import etree
import  time
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}




url = 'http://xin.cwan.com/'
html = requests.get(url, headers=headers)
html = html.content.decode('utf-8')
# text/html; charset=gb2312
print('网页\n',html)
doc = etree.HTML(html)

res = doc.xpath('//div[@class="tap-body list-a"]/dl/dd/h2/a/text()')
for i in res:
    print('爬取的数据:\n',i)

img = res = doc.xpath('//div[@class="tap-body list-a"]/dl/dt/a/img/@src')
dir_name = '资源包'
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
for i_img in res:
    # img_src = i_img.xpath('a/img/@src')[0]
    print(i_img)

newsDetail = res = doc.xpath('//div[@class="tap-body list-a"]/dl/dd/p/text()')
for i_newDetail in newsDetail:
    print('爬取的新闻详情:\n',i_newDetail)
newTimer = res = doc.xpath('//div[@class="tap-body list-a"]/dl/dd/label/span/span/text()')
for i_newTimer in newTimer:
    print('爬取的新闻详情:\n',i_newTimer)
