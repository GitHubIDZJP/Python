import parsel
import requests
# 使用 lxml
from lxml import etree
import  time
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
def get_page(page):
    url='https://www.kuaidaili.com/free/inha/'+str(page)
    response=requests.get(url,headers=headers)
    #数据类型转换
    html = parsel.Selector(response.text)
    parse_page(html)
def parse_page(html):
    #XPath的匹配范围 3层
    parse_list = html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    for tr in parse_list:
        #一层

        parse_lists = {}
        #extract_first():这个方法返回的是一个string字符串,是list数组里面的第一个字符串
        http = tr.xpath('./td[@data-title="类型"]//text()').extract_first()
        num = tr.xpath('./td[@data-title="IP"]//text()').extract_first()
        port = tr.xpath('./td[@data-title="PORT"]//text()').extract_first()
        parse_lists[http] = num + ':' + port
        time.sleep(0.1)
        print(parse_lists)
if __name__ == '__main__':
    for page in range(1,3):
        get_page(page)
    #url: https://www.kuaidaili.com/free/inha/任意数字
    #

'''
{'HTTP': '121.13.252.61:41564'}
{'HTTP': '61.216.156.222:60808'}
{'HTTP': '61.216.185.88:60808'}
{'HTTP': '121.13.252.58:41564'}
{'HTTP': '121.13.252.60:41564'}
{'HTTP': '210.5.10.87:53281'}
{'HTTP': '117.41.38.16:9000'}
{'HTTP': '183.236.232.160:8080'}
{'HTTP': '121.13.252.62:41564'}
{'HTTP': '112.14.47.6:52024'}
{'HTTP': '117.114.149.66:55443'}
{'HTTP': '222.74.73.202:42055'}
{'HTTP': '202.109.157.64:9000'}
{'HTTP': '202.109.157.62:9000'}
{'HTTP': '182.34.17.104:9999'}
{'HTTP': '27.42.168.46:55481'}
{'HTTP': '121.13.252.61:41564'}
{'HTTP': '61.216.156.222:60808'}
{'HTTP': '61.216.185.88:60808'}
{'HTTP': '121.13.252.58:41564'}
{'HTTP': '121.13.252.60:41564'}
{'HTTP': '210.5.10.87:53281'}
{'HTTP': '116.9.163.205:58080'}
{'HTTP': '183.236.232.160:8080'}
{'HTTP': '121.13.252.62:41564'}
{'HTTP': '112.14.47.6:52024'}
{'HTTP': '117.114.149.66:55443'}
{'HTTP': '222.74.73.202:42055'}
{'HTTP': '202.109.157.61:9000'}
{'HTTP': '117.41.38.19:9000'}


'''