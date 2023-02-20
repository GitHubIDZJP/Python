import requests
from bs4 import BeautifulSoup
# 给chat gpt提问:我想用python爬取豆瓣电影top250的数据，代码应该怎么写
# 这是用chat gpt爬取的 但是得自己加headers，不然爬取的数据为空
myHeaders = {
    'User-Agent':'Chrome/108.0.0.0'
}
# 请求URL
url = 'https://movie.douban.com/top250'

# 发送请求
response = requests.get(url,headers=myHeaders)

# 解析HTML
soup = BeautifulSoup(response.content, 'html.parser')

# 提取数据
movies = soup.find_all('div', class_='info')

# print('电影:\n',movies)
for movie in movies:
    title = movie.find('span', class_='title').get_text()
    info = movie.find('div', class_='bd').find('p').get_text().strip()
    rating = movie.find('span', class_='rating_num').get_text()
    quote = movie.find('span', class_='inq').get_text() if movie.find('span', class_='inq') else ''
    # print(title,info,rating,quote)
    print('1',title)
    print('2',info)
    print('3',rating)
    print('4',quote)

'''
举例说第一行的对应数据吧:
title = movie.find('span', class_='title').get_text() 
肖申克的救赎
info = movie.find('div', class_='bd').find('p').get_text().strip()
导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...
rating = movie.find('span', class_='rating_num').get_text()
9.7
quote = movie.find('span', class_='inq').get_text() if movie.find('span', class_='inq') else ''
希望让人自由。
'''