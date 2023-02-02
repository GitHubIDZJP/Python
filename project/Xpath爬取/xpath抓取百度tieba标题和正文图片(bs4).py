import requests
from bs4 import BeautifulSoup

#还没细看

class TiebaSpider:
    def __init__(self, name):
        self.start_url = "https://tieba.baidu.com/f?kw=" + name + "&ie=utf-8&pn=0"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
            # "Cookie": "你的cookie"
            "Cookie": "TIEBA_USERTYPE=b91d64da541da51f773ffed5"
        }

    def paser_url(self, url):  # 发送请求，获取响应
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    # 第一种方法：正则表达式
    # 第二种方法：xpath提取
    # 第三种方法：bs4提取
    def get_content_list(self, html_str):
        # 数据隐藏在注释里，取消注释标识
        html = html_str.replace('<!--', '').replace('-->', '')
        html = BeautifulSoup(html, "lxml")
        div_list = html.find_all('li', class_="j_thread_list clearfix thread_item_box")
        print(len(div_list))

        resp = []
        for h in div_list:
            title = h.find('div').find('a').text
            img = h.find_all('img')
            # title = h.xpath('.//div/a/text()')[0]
            # img = h.xpath('.//ul//img/@bpic')
            img = img[0].get('bpic') if img else ''
            resp.append((title,img))
        print(resp)
        for i in resp:
            print(i)

    def run(self):
        # 1.start_url
        # 2.发送请求，获取响应
        html_str = self.paser_url(self.start_url)
        # print(html_str)
        # 3.提取数据，提取下一页的url地址
        self.get_content_list(html_str)

        # 4.保存数据


if __name__ == '__main__':
    tieba_spider = TiebaSpider("李毅")
    tieba_spider.run()