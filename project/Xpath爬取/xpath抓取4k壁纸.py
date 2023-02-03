import requests
from lxml import etree
from fake_useragent import UserAgent
import time

#成功爬取(s4K壁纸)


'''
网址的变化:
https://wallhaven.cc/search?q=id%3A65348&page=1
https://wallhaven.cc/search?q=id%3A65348&page=2
https://wallhaven.cc/search?q=id%3A65348&page=3
滑动下一页时，每增加一页page自增加1，用{}代替变换的变量，再用for循环遍历这网址，实现多个网址请求
'''

# 1 定义一个class类继承object，定义init方法继承self，主函数main继承self。导入需要的库和网址
class wallhaven(object):
    def __init__(self):
        self.url = "https://wallhaven.cc/search?q=id%3A65348&page={}"
        # 2 fake_useragent模块实现随机产生UserAgent
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,

            }
        # print(self.headers)

    ''' 4 ----发送请求  获取响应'''

    def get_page(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.content.decode("utf-8")
        return html
        '''解析数据'''

    # 5 解析一级页面，得到二级页面的 href 地址
    def parse_page(self, html):
        parse_html = etree.HTML(html)
        image_src_list = parse_html.xpath('//figure//a/@href')
        # 6 遍历二级页面网址，发生请求、解析数据。找到相对于的图片地址
        for i in image_src_list:
            html1 = self.get_page(i)  # 第二个发生请求
            parse_html1 = etree.HTML(html1)
            # print(parse_html1)
            filename = parse_html1.xpath('//div[@class="scrollbox"]//img/@src')
            # print(filename)

            # 7  获取到的图片地址，发生请求，保存。图片地址发生请求
            for img in filename:
                # dirname = "/Users/zoujunping/python采集资源/采集01/图片" + img[32:]
                dirname = "../资源包/" + img[32:]
                html2 = requests.get(url=img, headers=self.headers).content
                with open(dirname, 'wb') as f:
                    f.write(html2)
                    print("%s下载成功" % dirname)

    #  3 for循环实现多网址访问。
    def main(self):
        startPage = int(input("4K起始页:"))
        endPage = int(input("4K终止页:"))
        for page in range(startPage, endPage + 1):
            url = self.url.format(page)
            # 8 调用方法，实现功能。
            html = self.get_page(url)
            self.parse_page(html)
            # 9 优化：设置延时。（防止ip被封）
            time.sleep(1.4)
            print("第%s页爬取成功！！！！" % page)


if __name__ == '__main__':
    imageSpider = wallhaven()
    imageSpider.main()
    print('结束执行')