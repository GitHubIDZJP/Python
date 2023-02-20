import requests
from lxml import etree
#海南政府采购网上商城
url = "http://zw.hainan.gov.cn/wssc/ec/jlyhnkj.html"
headers = {
    'User-Agent':'Chrome/108.0.0.0'
}
resp = requests.get(url,headers=headers)
text = resp.text
parse = etree.HTML(text)
#商品价格
price = parse.xpath("//div[@class='productlist']/ul/li/div[4]/text()")
print(type(price),len(price))
# print(price)
for i in price:
    print(i.strip().replace('\n',''))