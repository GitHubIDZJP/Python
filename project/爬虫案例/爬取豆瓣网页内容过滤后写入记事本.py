# from urllib.est import urlopen, Request
import csv

import requests
from  bs4 import  BeautifulSoup

# 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
url = 'https://read.douban.com/provider/all'

myHeaders = {
    'User-Agent':'Chrome/108.0.0.0'
}



# 打印网页源代码-HTML
# print(result.text)
# html=result.text

# soup=BeautifulSoup(html,'lxml')






result = requests.get(url, headers=myHeaders)  # HTTP GET POST PUT
print(result.status_code)

#最外层class值media
soup = BeautifulSoup(result.text, 'lxml')
fecthAll_Arr=soup.findAll('ul',class_='provider-items')
news_dict_list = [] #空数组 
for book in fecthAll_Arr:
#for打印标签元素
    title = book.find('a',class_='provider-item').text.strip()
    author = book.find('div',class_='name').text.strip()#.strip()去掉空格
    price = book.find('div',class_='works-num').text.strip()  #.find('a').text.strip()
    # fo = open("/Users/zoujunping/python采集资源/豆瓣排行榜/info2.csv", "w", newline='')

    #为保存文档做准备1
    news = {"标题": title, "发布时间": author,"发布时间1": price}
    news_dict_list.append(news)
    #2创建csv
    # fo = open("./news.txt", "w", newline='', encoding='utf-8')
    fo = open("/Users/zoujunping/python采集资源/豆瓣排行榜/news.txt", "w", newline='', encoding='utf-8')
    #3表头
    header = ["标题", "发布时间","发布时间1"]
    writer = csv.DictWriter(fo, header)
    #4写入表头
    writer.writeheader()
    #5将上一步的字典写入csv文件中
    writer.writerows(news_dict_list)
    #6关闭
    fo.close()

    print(title,author,price)
    print('*'*30)



print('数组长度:' + str(len(fecthAll_Arr)))





