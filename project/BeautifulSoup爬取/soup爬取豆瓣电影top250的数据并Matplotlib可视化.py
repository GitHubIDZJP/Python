
# pip install requests
# pip install beautifulsoup4
# pip install matplotlib
import  requests
import matplotlib
from bs4 import BeautifulSoup

import requests

url = 'https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
response = requests.get(url, headers=headers)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movie_list = soup.find('ol', class_='grid_view').find_all('li')[:20]

movies = []
for movie in movie_list:
    rank = movie.find('em').get_text()
    title = movie.find('span', class_='title').get_text()
    rating = movie.find('span', class_='rating_num').get_text()
    year = movie.find('span', class_='inq').get_text()
    print(rank,title,rating,year)
    movies.append({'rank': rank, 'title': title, 'rating': rating, 'year': year})


print('数据长度',len(movies))
# for i_movies in  movies:
#     print("数据:\n",i_movies)
import matplotlib

import matplotlib.pyplot as plt

font = {
    "family": "Microsoft SimHei"
}
matplotlib.rc("font", **font)
print (matplotlib.matplotlib_fname()) # 将会获得matplotlib配置文件

ratings = [float(movie['rating']) for movie in movies]
titles = [movie['title'] for movie in movies]
# plt.xticks(x,xtick_labels,fontproperties=my_font)
plt.bar(range(len(ratings)), ratings, tick_label=titles)
plt.xticks(rotation=90)
plt.xlabel('Movie Title')
plt.ylabel('Rating')
plt.title('豆瓣20强电影')
# plt.rcParams['font.sans-serif']=['cmb10']
plt.show()


#操作路径；
# /User/zoujunping/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/matplotlib/mpl-data

'''
解决可视化中文乱码:
删除 rm -rf /Users/zoujunping/.matplotlib
# 去掉前面的#号
font.family:  sans-serif
# 去掉前面的#号，并在:号后面加上SimHei
font.sans-serif: SimHei, DejaVu Sans, Bitstream Vera Sans, Computer Modern Sans Serif, Lucida Grande, Verdana, Geneva, Lucid, Arial, Helvetica, Avant Garde, sans-serif
# 去掉前面的#号，并将True改为False
axes.unicode_minus: False
链接：
1.
https://blog.csdn.net/weixin_44225182/article/details/119764954
2.
https://huaweicloud.csdn.net/63806bdedacf622b8df87abd.html?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2~default~BlogCommendFromBaidu~activity-1-124238611-blog-119764954.pc_relevant_vip_default&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2~default~BlogCommendFromBaidu~activity-1-124238611-blog-119764954.pc_relevant_vip_default&utm_relevant_index=1
先看1再看2 1和2结合使用就能解决

'''