# 豆瓣读书


# 使用 urllib
import requests
# 使用 lxml
from lxml import etree

# 定义 header


# 1、定义一个 https 的 url
# url = 'https://read.douban.com/provider/all'
# #2
# result = requests.get(url, headers=headers)  # HTTP GET POST PUT
# print(result.status_code)

import requests
from bs4 import BeautifulSoup
for page in range(1, 51):
    url = f'https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&p={page}'
    headers = {
        # UA 最基本的防爬识别
        'User-Agent':'Chrome/108.0.0.0'
    }
    response = requests.get(url,headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    book_titles = soup.select('.title > a')
    for title in book_titles:
        print(title['title'])
