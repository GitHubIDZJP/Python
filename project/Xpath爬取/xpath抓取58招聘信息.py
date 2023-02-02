'''
前言:
软件：PyCharm
需要的库：requests、lxml、fake_useragent
网站如下
https://gz.58.com/job/pn2/?param7503=1&from=yjz2_zhaopin&PGTID=0d302408-0000-3efd-48f6-ff64d26b4b1c&ClickID={}
ClickID={}每增加一页自增加1，用{}代替变换的变量，再用for循环遍历这网址，实现多个网址请求
'''

'''
反爬措施：
该网站上的反爬主要有两点：
1、 直接使用requests库，在不设置任何header的情况下，网站直接不返回数据
2、同一个ip连续访问多次，直接封掉ip，起初我的ip就是这样被封掉的。

为了解决这两个问题，最后经过研究，使用以下方法，可以有效解决。
1、获取正常的 http请求头，并在requests请求时设置这些常规的http请求头。
2、使用 fake_useragent ，产生随机的UserAgent进行访问。
'''

'''
实现思路:
1.定义一个class类继承object，定义init方法继承self，主函数main继承self。导入需要的库和网址
2.随机产生UserAgent。
3.随机产生UserAgent。
4.xpath解析找到对应的父节点
5.for遍历，定义一个变量food_info保存，获取到二级页面对应的菜 名、 原 料 、下 载 链 接。
6.将结果保存在txt文档中
7.调用方法，实现功能
'''
#没
import requests
from lxml import etree
from fake_useragent import UserAgent


# 网站  ： url
# 1、定义一个class类继承object，定义init方法继承self，主函数main继承self。导入需要的库和网址
class Zhaopin(object):
    def __init__(self):
        self.url = "https://gz.58.com/job/pn2/?param7503=1&from=yjz2_zhaopin&PGTID=0d302408-0000-3efd-48f6-ff64d26b4b1c&ClickID={}"  # /zhuanchang/:搜索的名字的拼音缩写
        ua = UserAgent(verify_ssl=False)
        #2. 随机产生UserAgent
        for i in range(1, 50):
            self.headers = {
                'User-Agent': ua.random,

            }
    #3 发送请求，获取响应, 页面回调，方便下次请求
    def get_page(self, url):
        req = requests.get(url=url, headers=self.headers)
        html = req.content.decode("utf-8")
        return html
    #4 xpath解析找到对应的父节点。
    def page_page(self, html):
        # 5 for遍历，定义一个变量food_info保存，获取到二级页面对应的菜 名、 原 料 、下 载 链 接。
        parse_html = etree.HTML(html)
        one = parse_html.xpath('//div[@class="main clearfix"]//div[@class="leftCon"]/ul/li')
        for l in one:
            o = l.xpath('.//a/span[1]/text()')[0].strip()
            t = l.xpath('.//a//span[@class="name"]/text()')[0].strip()
            f = l.xpath('.//p[@class="job_salary"]/text()')
            thr = l.xpath('.//div[@class="comp_name"]//a/text()')[0].strip()
            # address = l.xpath('//div[@class="list_con"]/ul/li/div/p/text()')
            # print('打印咨询你')
            # # print(address)
            # for a in  address:
            #     print('薪资:\n',a)
            for e in f:
                print(e)
                boss = '''  
 %s:||%s: 
 公司：%s,
 工资：%s元/月
 =========================================================
                                ''' % (o, t, thr, e)
            # print(o)
            # print(t)
            # print(thr)
            # print(e)
            # 6 将结果保存在txt文档中
            f = open('g.txt', 'a', encoding='utf-8')  # 以'w'方式打开文件
            f.write(str(boss))
            print(str(boss))
            f.write("\n")  # 键和值分行放，键在单数行，值在双数行
            f.close()

    def main(self):
        stat = int(input("输 入 开 始 （2开始）:"))
        end = int(input("输 入 结 束:"))
        for page in range(stat, end + 1):
            url = self.url.format(page)
            print(url)
            # 6 调用方法，实现功能
            html = self.get_page(url)
            self.page_page(html)
            # print("==================第%s页爬取成功！！！！=====================" % page)

            # print(tree)
            # res = doc.xpath('//div[@class="list_con"]/ul/li/div/p/text()')


if __name__ == '__main__':
    Siper = Zhaopin()
    Siper.main()


