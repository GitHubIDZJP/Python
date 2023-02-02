# 使用 urllib
import requests
# 使用 lxml
from lxml import etree

# 定义 header
headers = {
  # UA 最基本的防爬识别
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

# 1、定义一个 https 的 url
url = 'https://read.douban.com/provider/all'
#2
result = requests.get(url, headers=headers)  # HTTP GET POST PUT
print(result.status_code)



tree = etree.HTML(result.content.decode('utf-8'))

# 是否存在 id 属性为 su 的标签
print(tree.xpath('//@id="su"')) # True


# 获得 `百度一下` 四个字
print(tree.xpath('//input[@id="su"]/@value')) # ['百度一下']


print(tree.xpath('//*[@id="_16727880778075_0"]/div/a/div[2]'))
li = tree.xpath('//div/div[not(@id) or @class="cm-body"]/text()')
for i in li:
  print(i)

#字母
letter = tree.xpath('//div/div/div/div[not(@id) or  @class="index-name"]/text()')
print(letter)

#备案信息
record_msg = tree.xpath('//div/div/div/div/a[not(@id) or  @class="name"]/text()')
print(record_msg )


#查询网页class为name的网页内容
book_name = tree.xpath('//div[@class="name"]/text()')
print(book_name)
#书名和在售书价一次性获取到 2个属性中间用or隔开就行
book_info = tree.xpath('//div[@class="name" or  @class="works-num"]/text()')
print(book_info)

#在售书本
selling_books = tree.xpath('//div[@class="works-num"]/text()')
print(selling_books)
#书首页图片
book_picture = tree.xpath('//div[@class="avatar"]/img/@src')
print(book_picture)

#获取图片相对链接地址
selling_books1 = tree.xpath('//ul[@class="provider-items"]/li/a/@href')

print(selling_books1)#因为是相对链接地址，所以获得的是/provider/63687123/











