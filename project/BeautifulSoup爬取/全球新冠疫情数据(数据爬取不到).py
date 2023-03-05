import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from lxml import etree
# myHeaders = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
#     'Cookie':'userid=1677592548071_s777p95837'
# }
url = 'https://news.ifeng.com/c/special/7tPlDSzDgVk?needpage=1&webkit=1'

ua = UserAgent(verify_ssl=False)
myHeaders = {
    'User-Agent':ua.random,
    'Cookie':'userid=1677592548071_s777p95837'
}
response = requests.get(url,headers=myHeaders)
response.content.decode('utf-8')
# print(response.content.decode('utf-8'))
print(response.status_code)
tree = etree.HTML(response.content.decode('utf-8'))
book_name = tree.xpath('//div[@class="index_data_box_fC61a index_local_EHE-M"]/div[@class="index_tr_list_4IrYQ"]/span/text()')
print(book_name)


# soup = BeautifulSoup(response.text, 'html.parser')
#
# # 获取标题
# title = soup.title.string
# print(title)
#
# attributes = soup.findAll('div',class_='index_tbody_7MZrG')
# print(attributes) #打印为[]
# for attribute in attributes:
#     country = attribute.find('span', class_=False)[1].text.strip()
#     print('国家',country)
#     numberOfInfectedPersons = attribute.find('span',class_=False)[2].text.strip()
#     print('累计确诊人数:',numberOfInfectedPersons)
#     deathToll = attribute.find('span',class_=False)[3].text.strip()
#     print('死亡人数',deathToll)


