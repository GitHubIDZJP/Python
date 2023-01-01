import requests
import parsel
import requests
# from urllib import request
from bs4 import BeautifulSoup
import time
import random
from random import randint
import requests
from bs4 import BeautifulSoup

def display(arc):

    # if __name__ == '__main__':
        # 1.对首页的页面信息进行爬取
        url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'}
        # print(page_text.encoding) #编码方式是：ISO-8859-1  pycharam只能显示utf-8
        page_text = requests.get(url=url, headers=headers).text
        page_text = page_text.encode('ISO-8859-1')  # encode编码，将ISO-8859-1编成unicode
        page_text = page_text.decode('utf-8')

        # 2.在首页中解析出章节的标题和详情页的url
        # （1）实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
        soup = BeautifulSoup(page_text, 'lxml')
        # (2)
        li_list = soup.select('.book-mulu > ul >li')
        # fp = open('./三国演义.txt', 'w', encoding='UTF-8') #存到项目本身
        fp = open('/Users/zoujunping/python采集资源/小说采集01/三国演义.txt', 'w', encoding='UTF-8') #存到自己指定的电脑路径
        for li in li_list:
            title = li.a.string
            detail_url = 'https://www.shicimingju.com' + li.a['href']
            # 对详情页发起请求,解析出章节内容
            detail_page_text = requests.get(url=detail_url, headers=headers).text
            detail_page_text = detail_page_text.encode('ISO-8859-1')
            detail_page_text = detail_page_text.decode('utf-8')

            # 解析出详情页中相关的章节内容
            detail_soup = BeautifulSoup(detail_page_text, 'lxml')
            div_tag = detail_soup.find('div', class_='chapter_content')
            content = div_tag.text
            # 存数据
            fp.write(title + ':' + content + '\n')
            # fp.write(f"/Users/zoujunping/python采集资源/小说采集01/{content}.txt" + ':' + title + '\n')
            print(title, '爬取成功')
            print("小说标题:\n",title)
            print("小说章节内容:\n",content)