url='https://book.jd.com/?cu=true&utm_source=www.baidu.com&utm_medium=tuiguang&utm_campaign=t_1003608409_&utm_term=f7046be968cc4ba4b623bfb019b2237f'






import requests
from bs4 import BeautifulSoup
# for page in range(1, 25):
#     url = f'https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&amp;p={page}'
headers = {
    # UA 最基本的防爬识别
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
}
response = requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')
# media clearfix
book_Arr = soup.findAll('div',class_='pd_pic_wrap')
# print(book_Arr)
print('数组长度:\n',len(book_Arr))
# for li in book_Arr:
#     a = li.find(name='a')
#     print('长度:\n',len(a))
#     h2 = str(li.find(name='h2').text)
#     print(h2)
    # p1 = li.find(name='p',class_="subject-abstract color-gray")
    # p2 = li.find(name='p', class_="clearfix w250")
    # span1 = li.find(name='span', class_="buy-info")
    # span2 = li.find(name='span', class_="cart-info")

    # print(title['title'])


# 一页20本书msg，500/20=25