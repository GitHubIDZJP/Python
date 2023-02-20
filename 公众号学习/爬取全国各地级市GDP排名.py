# import requests
# from lxml import etree
# import csv
# import time
# import pandas as pd
#
#
# def gdpData(page):
#     url = f'https://www.hongheiku.com/category/gdjsgdp/page/{page}'
#     headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
#     resp = requests.get(url,headers = headers)
# # print(resp.text)
#     data(resp.text)
# file = open('data.csv',mode='a',encoding='utf-8',newline='')
# csv_write=csv.DictWriter(file,fieldnames=['排名','地区','GDP','年份'])
# csv_write.writeheader()
# def data(text):
#     e = etree.HTML(text)
#     lst = e.xpath('//*[@id="tablepress-48"]/tbody/tr[@class="even"]')
#     for l in lst:
#         no = l.xpath('./td[1]/center/span/text()')
#         name = l.xpath('./td[2]/a/center/text()')
#         team = l.xpath('./td[3]/center/text()')
#         year = l.xpath('./td[4]/center/text()')
#         data_dict = {
#             '排名':no,
#             '地区':name,
#             'GDP':team,
#             '年份':year
#         }
#         print(f'排名：{no} 地区:{name} GDP:{team} 年份:{year} ')
#         csv_write.writerow(data_dict)
# file.close()
# url = 'https://www.hongheiku.com/category/gdjsgdp'
# headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
# resp = requests.get(url,headers=headers)
#
# # print(resp.text)
# data(resp.text)
# e = etree.HTML(resp.text)
# #//*[@id="tablepress-48"]/tbody/tr[192]/td[3]/center
# count = e.xpath('//div[@class="pagination pagination-multi"][last()]/ul/li[last()]/span/text()')[0].split(' ')[1]
# for index in range(int(count) - 1):
#     gdpData(index + 2)

import requests
import pandas as pd
url = 'https://www.hongheiku.com/category/gdjsgdp'
headers ={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
resp = requests.get(url,headers = headers)
df = pd.read_html(resp.text)[0].dropna()
df.to_excel('1.xlsx',index=None)
print("获取值:\n",df)

# dropna()函数的作用是去除读入的数据中（DataFrame）含有NaN的行