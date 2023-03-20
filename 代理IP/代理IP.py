import requests
import parsel
import time

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36'
}
def get_page(page):
    url='https://www.kuaidaili.com/free/inha/'+str(page)
    response=requests.get(url,headers=headers)
    # 数据类型转换
    html = parsel.Selector(response.text)
    parse_page(html)

def parse_page(html):
    #XPath的匹配范围
    parse_list = html.xpath('//table[@class="table table-bordered table-striped"]/tbody/tr')
    for tr in parse_list:
        parse_lists = {}
        http=tr.xpath('./td[@data-title="类型"]//text()').extract_first()
        num=tr.xpath('./td[@data-title="IP"]//text()').extract_first()
        port=tr.xpath('./td[@data-title="PORT"]//text()').extract_first()
        parse_lists[http]=num+':'+port
        time.sleep(0.1)
        print(parse_lists)

if __name__ == '__main__':
    for page in range(1,3):
        get_page(page)
'''

{'HTTP': '222.74.73.202:42055'}
{'HTTP': '182.34.17.104:9999'}
{'HTTP': '121.13.252.62:41564'}
{'HTTP': '61.164.39.68:53281'}
{'HTTP': '27.42.168.46:55481'}
{'HTTP': '121.13.252.58:41564'}
{'HTTP': '61.216.185.88:60808'}
{'HTTP': '183.236.232.160:8080'}
{'HTTP': '116.9.163.205:58080'}
{'HTTP': '210.5.10.87:53281'}
{'HTTP': '121.13.252.60:41564'}
{'HTTP': '117.114.149.66:55443'}
{'HTTP': '61.216.156.222:60808'}
{'HTTP': '112.14.47.6:52024'}
{'HTTP': '121.13.252.61:41564'}
{'HTTP': '113.124.86.24:9999'}
{'HTTP': '222.74.73.202:42055'}
{'HTTP': '182.34.17.104:9999'}
{'HTTP': '121.13.252.62:41564'}
{'HTTP': '61.164.39.68:53281'}
{'HTTP': '27.42.168.46:55481'}
{'HTTP': '121.13.252.58:41564'}
{'HTTP': '61.216.185.88:60808'}
{'HTTP': '183.236.232.160:8080'}
{'HTTP': '116.9.163.205:58080'}
{'HTTP': '210.5.10.87:53281'}
{'HTTP': '121.13.252.60:41564'}
{'HTTP': '117.114.149.66:55443'}
{'HTTP': '61.216.156.222:60808'}
{'HTTP': '112.14.47.6:52024'}

'''