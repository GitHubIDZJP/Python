import requests
from lxml import etree
from fake_useragent import UserAgent
import time


#点击下一页时，每增加一页page自增加1，用{}代替变换的变量，再用for循环遍历这网址，实现多个网址请求

'''
反爬措施的处理

主要有两个点需要注意：
1、直接使用requests库，在不设置任何header的情况下，网站直接不返回数据
2、同一个ip连续访问多次，直接封掉ip，起初我的ip就是这样被封掉的。
 为了解决这两个问题，最后经过研究，使用以下方法，可以有效解决。
1）获取正常的 http请求头，并在requests请求时设置这些常规的http请求头。
2）使用 fake_useragent ，产生随机的UserAgent进行访问

'''

#1定义一个class类继承object，定义init方法继承self，主函数main继承self。
# 1.1 导入需要的库和网址，代码如下所示。
class kitchen(object):
    # 方法二 8.2：定义一个变量u,for遍历，表示爬取的是第几种食物
    u = 0;

    def __init__(self):
        self.url = "https://www.xiachufang.com/explore/?page={}"
        ua = UserAgent(verify_ssl=False)
        # 2 随机产生UserAgent
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,

            }

    '''发送请求  获取响应'''

    # 3、发送请求,获取响应, 页面回调，方便下次请求

    def get_page(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content.decode("utf-8")
        return html
        '''解析数据'''

    # 4 xpath解析一级页面数据,获取二级页面网址。

    def parse_page(self, html):
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//li/div/a/@href')

        # 5.  for遍历，定义一个变量food_info保存，获取到二级页面对应的菜名、 原料 、下载链接
        for i in image_src_list:
            url = "https://www.xiachufang.com/" + i
            # print(url)
            html1 = self.get_page(url)  # 第二个发生请求
            parse_html1 = etree.HTML(html1)
            # print(parse_html1)

            num = parse_html1.xpath('.//h2[@id="steps"]/text()')[0].strip()
            name = parse_html1.xpath('.//li[@class="container"]/p/text()')
            ingredients = parse_html1.xpath('.//td//a/text()')

            # 方法二8.3：定义一个变量u, for遍历，表示爬取的是第几种食物
            self.u += 1;
            # print(self.u)
            # print(str(self.u)+"."+house_dict["名 称 :"]+":")
            # da=tuple(house_dict["材 料:"])
            food_info = '''  
第 %s 种

菜 名 : %s
原 料 : %s
下 载 链 接 : %s,
=================================================================
                    ''' % (str(self.u), num, ingredients, url)
            # print(food_info)

            # 6 保存在world文档
            f = open('菜谱.doc', 'w', encoding='utf-8')  # 以'w'方式打开文件
            f.write(str(food_info))
            print(str(food_info))
            f.close()

    def main(self):
        startPage = int(input("起始页:"))
        endPage = int(input("终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            # 7 调用方法，实现功能
            html = self.get_page(url)
            self.parse_page(html)
            # 8项目优化
            # 8.1方法一：设置时间延时
            time.sleep(1.4)
            print("====================================第 %s 页 爬 取 成 功====================================" % page)


if __name__ == '__main__':
    imageSpider = kitchen()
    imageSpider.main()