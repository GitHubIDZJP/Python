

#
import openpyxl
import parsel
import requests
import pandas as pd
import csv
# 使用 lxml
from lxml import etree
import  time
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}


url = 'http://www.xiaohua.com/duanzi/'
html = requests.get(url, headers=headers)
html = html.content.decode('utf-8')
# text/html; charset=gb2312
doc = etree.HTML(html)
# print(tree)
res = doc.xpath('//div[@class="one-cont"]/p/a/text()')
for i in res:
    print('爬取的数据:\n',i)
    with open('./笑话网.csv', 'a', encoding='utf8') as f:
        f.write(i + '\n')