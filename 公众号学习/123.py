import struct

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
#商品价格 --选择器Xpath提取规则写的有问题，下面更改1 已经更改，div[4] 有几个价格不在4个div里
# price = parse.xpath("//div[@class='productlist']/ul/li/div[4]/text()")
#更改1
price = parse.xpath("//div[@class='product_price']/text()") #直接一步到位
print(type(price),len(price))
# print(price)
# for i in price:
#     print(i.strip().replace('\n',''))
#更改2--内置函数，剔除2边的空字符 换行符
for i in map(str.strip,filter(str.strip,price)):
    print(i)

    # replace('\n','')去掉换行符
    #strip()去掉空格

    '''
    打印时 每2个时间之间会有个空行
    更改1和更改2则
    ¥35,000.00
    ¥2,999.00
    ¥33,200.00
    ¥3,999.00
    ¥12,000.00
    ¥1,990.00
    ¥27,550.00
    ¥1,710.00
    ¥1,100.00
    ¥4,500.00

    '''


    '''
    新方法1：
    resp = requests.get(url, headers=headers)
    text = resp.text
    parse = etree.HTML(text)
    price = parse.xpath("//div[@class='product_price']/text()")
    print(type(price), len(price))
    for i in price:
        if i.strip():
            print(i.replace('\n', '').strip())
    '''


    '''
    新方法2：
    url = "http://zw.hainan.gov.cn/wssc/ec/jlyhnkj.html"
    resp = requests.get(url)
    text = resp.text
    parse = etree.HTML(text)
    price = parse.xpath("//div[@class='productlist']/ul/li/div[4]/text()")
    # 直接使用列表推导式，去掉冗余数据
    price = [i.strip() for i in price if i.strip()]
    print(price)
    # 为了方便统计，再去掉￥符号，再转换成数字
    # price = [int(float(i.replace('¥', '').replace(',', ''))) for i in price]
    # 或者用re.sub去掉多余符号，再转换成数字，上下两种方法，选一个就行
    # 需要import re
    # price = [int(float(re.sub(r'[¥,]', '', i))) for i in price]
    print(price)
    '''