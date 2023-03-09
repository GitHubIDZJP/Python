import requests
from bs4 import BeautifulSoup

import pymysql
# 1
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='pdb',
    charset='utf8',
    autocommit=True
)
#2 光标
cursor = conn.cursor(pymysql.cursors.DictCursor)#生成游标对象


# 网站:汽车之家
url = 'https://www.autohome.com.cn/news/2/#liststart'
headers = {
     'User-Agent':'Chrome/108.0.0.0'
}
result = requests.get(url,headers=headers)
# print(result.status_code)
soup = BeautifulSoup(result.text,'html.parser')
#下面2个都可以
# li_list = soup.find('div',class_='article-wrapper').find_all('li')
li_list = soup.find('ul',class_='article').find_all('li')
# print(li_list)
for li in li_list:
     #通过name查找元素
     h3 = li.find(name='h3')
     if not h3:
          continue
     title = h3.text
     # print(title)
     #通过class查找元素
     # title = li.find('h3', class_=False).text.strip()#str(li.find(name='h3').text)
     # print(title)
     desc = str(li.find(name='p').text)
     # print(desc)
     img = 'https:' + li.find(name='img')['src']
     # print(img)
     url = 'https:' + li.find(name='a')['href']
     # print(url)
     print(f'''
         新闻标题：{title}
         新闻摘要：{desc}
         新闻链接：{url}
         新闻图片：{img}
         ''')
     # 3
     # sql = 'insert into python_table(title,content,url,img) values(%s,%s,%s,%s)'
     sql = 'insert into push_db(title,content,url,img) values(%s,%s,%s,%s)'
     # 4
     cursor.execute(sql, (title, desc, url, img))
# 5
cursor.close()
# 6
conn.close()

'''
在db1-pdb数据库下python_table表里创建字段
名      类型      长度  小数点 部署null  健  注释
id      int       50    0     √        1   id值      自动递增要勾选上
title   varchar   255         √                      默认值 字符集 排序规则 二进制 都不勾选
content  varchar   255         √                      默认值 字符集 排序规则 二进制 都不勾选
url   varchar   255         √                      默认值 字符集 排序规则 二进制 都不勾选
img   varchar   255         √                      默认值 字符集 排序规则 二进制 都不勾选

点击保存
主要是id，一定要勾选自动递增
'''


#操作数据库


