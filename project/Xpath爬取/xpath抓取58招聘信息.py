import requests
from lxml import etree


# from fake_useragent import UserAgent
# from hyper.contrib import HTTP20Adapter


# 网站  ： url
class Zhaopin(object):
    def __init__(self):
        self.url = "https://gz.58.com/job/pn2/?param7503=1&from=yjz2_zhaopin&PGTID=0d302408-0000-3efd-48f6-ff64d26b4b1c&ClickID={}"  # /zhuanchang/:搜索的名字的拼音缩写
        # ua = UserAgent(verify_ssl=False)
        # for i in range(1, 50):
        self.headers = {
            # 'User-Agent': ua.random,

            'authority': 'gz.58.com',
            'method': 'GET',
            # 'path': '/job/pn2/?param7503=1&from=yjz2_zhaopin&PGTID=0d302408-0000-3efd-48f6-ff64d26b4b1c&ClickID=1',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'referer': 'https://gz.58.com/',
            'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'upgrade-insecure-requests': '1',
            # 'cookie': 'sessionid=a9dd023f-ff80-47dd-8694-91e55f5710a7; id58=udXymGPek/04Z0eUG0DkAg==; wmda_uuid=12033ecf811d59c49dd4dec044c3f712; wmda_new_uuid=1; 58tj_uuid=ba48af68-95b1-4e71-af59-986ffeff41d5; 58home=bj; als=0; __bid_n=18543191897e243c0f4207; wmda_visited_projects=;1731916484865;11187958619315; xxzl_deviceid=SoWFFK9HSEArHn65YoQK6g5bjtGHTtbhtCDof+jaeHNALEuauHPHgcGC00rqr91u; crmvip=; dk_cookie=; www58com="UserID=27569343660038&UserName=qqfku_f2"; 58cooper="userid=27569343660038&username=qqfku_f2"; 58uname=qqfku_f2; passportAccount="atype=0&bstate=0"; webimwmda=63de95f315fdb303b1572a05; xxzl_smartid=8edd77de69a2341e639f06b406b167ce; PPU=UID=27569343660038&UN=qqfku_f2&TT=16cf9868f95a98726b2e14b3969eb9bc&PBODY=eRDosQ7uRUnuqtQeHb1bg-pGNmJaLvQ5DZ7Y0_HU6WECzMdcU-lC0x_XC7q69FtLQojoQhwE3xt11IpeGV-D5KMC5u6n5NFSjtb0dswiec_sMvOhyuqWokmgTHAiSrA0phHEqwwHQ687cnoWZUf8LrxP8H2NbX7GB9YfxrjgFGw&VER=1&CUID=--M140jsKGI6fI6xqdI20w; fzq_h=a35961acc2c835b0faa21881cd299fb5_1675772740292_51370a75f32d488b858adb0d1ae2236b_47896383520923175131528915946346285496; wmda_session_id_1731916484865=1675772762399-3db39539-be85-b052; new_uv=2; utm_source=; spm=; init_refer=; commontopbar_new_city_info=1|北京|bj; FPTOKEN=OCaPzM1irdx47+sGvoPKdajuwjzS/jhAWxmE91O3NmR0XPpPHB7QO8Ws+SrUrslBIoFWb0nle+pJ42UYBfo5Qqt9ESDKvtJk8dufyfI1d7vXqZSvUujuCoUH3ig3I3vcrDqHuSXjHc0aMmoYLQptcBLlWayw/sPEEnYUzl97dugpemKB5FG9cncvQKz+P7hYzcBO/ZRZgIp+ApIB33NORRTA9lbI9mPlIRZtrpE8fiouuRGImasSZJUhIm4FQZRkX1BXbXVqq7RTlYt98ATiLoyQmK0HXXPZaYup2BIUie1g+cy3fI2C7atgjcO7xrzfZ6tPBahie0NMvgQTnGUoqlkVF53zwc1kCyLLR5vKQOISyt5NlrijS/GH88J13IJa3C4UstcgMxNj6THadXPSJJHaHQD5DMSlVWA4jdiNw0PCR3cOLjxxzlxLPhc/hjok|LLUiODRhU2ozYy0yWc4ACNj33PCUk7TOEHHTiERIYmI=|10|6a5aab5e3484a53197bfe6a040082cd2; wmda_session_id_11187958619315=1675772776027-0d2f3517-5128-0653; new_session=0',
            'cookie': '_f2"; 58uname=qqfku_f2; passportAccount="atype=0&bstate=0"; xxzl_smartid=8edd77de69a2341e639f06b406b167ce; PPU=UID=27569343660038&UN=qqfku_f2&TT=16cf9868f95a98726b2e14b3969eb9bc&PBODY=eRDosQ7uRUnuqtQeHb1bg-pGNmJaLvQ5DZ7Y0_HU6WECzMdcU-lC0x_XC7q69FtLQojoQhwE3xt11IpeGV-D5KMC5u6n5NFSjtb0dswiec_sMvOhyuqWokmgTHAiSrA0phHEqwwHQ687cnoWZUf8LrxP8H2NbX7GB9YfxrjgFGw&VER=1&CUID=--M140jsKGI6fI6xqdI20w; fzq_h=a35961acc2c835b0faa21881cd299fb5_1675772740292_51370a75f32d488b858adb0d1ae2236b_47896383520923175131528915946346285496; FPTOKEN=OCaPzM1irdx47+sGvoPKdajuwjzS/jhAWxmE91O3NmR0XPpPHB7QO8Ws+SrUrslBIoFWb0nle+pJ42UYBfo5Qqt9ESDKvtJk8dufyfI1d7vXqZSvUujuCoUH3ig3I3vcrDqHuSXjHc0aMmoYLQptcBLlWayw/sPEEnYUzl97dugpemKB5FG9cncvQKz+P7hYzcBO/ZRZgIp+ApIB33NORRTA9lbI9mPlIRZtrpE8fiouuRGImasSZJUhIm4FQZRkX1BXbXVqq7RTlYt98ATiLoyQmK0HXXPZaYup2BIUie1g+cy3fI2C7atgjcO7xrzfZ6tPBahie0NMvgQTnGUoqlkVF53zwc1kCyLLR5vKQOISyt5NlrijS/GH88J13IJa3C4UstcgMxNj6THadXPSJJHaHQD5DMSlVWA4jdiNw0PCR3cOLjxxzlxLPhc/hjok|LLUiODRhU2ozYy0yWc4ACNj33PCUk7TOEHHTiERIYmI=|10|6a5aab5e3484a53197bfe6a040082cd2; JSESSIONID=6F107DEA3C1A1193CFC59D1131D1CE10; new_uv=3; fzq_js_zhaopin_list_pc=485df0d102e33af99b31649780357ee6_1675778705499_7; Hm_lpvt_5bcc464efd3454091cf2095d3515ea05=1675778706',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

        }

    def get_page(self, url):
        session = requests.Session()
        # session.mount('https://webim.58.com',HTTP20Adapter())
        # req = requests.get(url=url, headers=self.headers)
        req = session.get(url=url, headers=self.headers)

        html = req.content.decode("utf-8")
        # print('网页',html)
        print('状态码:', req.status_code, "null")
        return html

    def page_page(self, html):
        parse_html = etree.HTML(html)
        print('网页',parse_html)
        # with open("page58.txt", "wb") as f:
        # 写文件用bytes而不是str，所以要转码
        #    f.write(html.encode())
        # item = parse_html.xpath('/div[@class="con"]/div/div/div/ul/li/div/a/span/text()')
        item = parse_html.xpath('//ul[@id="list_con"]/li')
        print('获取data:\n',item) #没获取到数据
        # for i in item:
        #     city = i.xpath('/div/div/a/span[0]/text()')
        #     print(city)

        for l in item:

            o = l.xpath('div[@class="job_name clearfix"]/text()')  # [0].strip()
            # o = l.xpath('div/div/a/span[1]/text()')[0].strip()
            print(o)
            t = l.xpath('.//a//span[@class="name"]/text()')[0].strip()
            print('公司福利\n',t)
            f = l.xpath('.//p[@class="job_salary"]/text()')
            print('公司名\n字',f)
            thr = l.xpath('.//div[@class="comp_name"]//a/text()')[0].strip()
            print('月薪:\n',thr)
            for e in f:
                boss = '''  

 %s:||%s: 
 公司：%s,
 工资：%s元/月
 =========================================================
                                ''' % (o, t, thr, e)
            # print(food_info)
            f = open('g.txt', 'a', encoding='utf-8')  # 以'w'方式打开文件
            f.write(str(boss))
            print(str(boss))
            f.write("\n")  # 键和值分行放，键在单数行，值在双数行
            f.close()

    def main(self):
        # stat = int(input("输 入 开 始 （2开始）:"))
        # end = int(input("输 入 结 束:"))
        # for page in range(stat, end + 1):
        for page in range(1, 4):
        # page = 2
            url = self.url.format(page)
            print(url)
            html = self.get_page(url)
            self.page_page(html)
            print("==================第%s页爬取成功！！！！=====================" % page)

        '''
        page = 2
        url = self.url.format(page)
        print(url)
        html = self.get_page(url)
        self.page_page(html)
        print("==================第%s页爬取成功！！！！=====================" % page)
        '''

if __name__ == '__main__':
    Siper = Zhaopin()
    Siper.main()
