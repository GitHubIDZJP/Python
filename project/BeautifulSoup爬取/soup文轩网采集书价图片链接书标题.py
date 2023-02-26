import requests
from bs4 import BeautifulSoup
myHeaders = {
    'User-Agent':'Chrome/108.0.0.0'
}
url = 'https://www.winxuan.com/'

response = requests.get(url,headers=myHeaders)
soup = BeautifulSoup(response.text, 'html.parser')

# 获取标题
title = soup.title.string
print(title)

# # 获取主图
# main_image = soup.find('img', {'class': 'banner-img'})['src']
# print(main_image)
#
# 获取属性
# attributes = soup.findAll('div', {'class': 'bt-row'}) 这样写class也可以的
attributes = soup.findAll('div',class_='common-module-2020-product')
print(attributes)
for attribute in attributes:

    # book_name = attribute.find('a',{'class':False})['href']
    book_name = attribute.find('div', class_='name').text.strip()
    print('书名',book_name)
    book_price_current = attribute.find('div',class_='price').find('span',class_='price-n').text.strip()
    print('现价:',book_price_current)
    book_price_old = attribute.find('div',class_='price').find('span',class_='price-o').text.strip()
    print('旧价',book_price_old)
    book_img = attribute.find('img')['data-original']
    print('图片图片',book_img)

'''
HTML里是；
<div class="bt-row"> 最外层 框框
 <div class="bt-col-2"> 倒数第2层
   <div class="common-module-2020-product"> 倒数第3层 ----->soup抓取数据时外层findAll时只要当前找到当前对应那行的div就行，然后for循环里再取挨个找对应的HTML和class或者ID就行，可以直接最外层到最里层，不想Xpath得直接一层一层去找
     <div class="name"> 倒数第4层 也是要取值的所在层
     <div>
   <div>
 <div>
</div>
获取所有class对应的name值的HTML元素
for循环依次打印

重点: 只需要获取最外层的那层 再获取对应的层HTML元素就行 
'''