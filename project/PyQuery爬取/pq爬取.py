import requests
from pyquery import PyQuery as pq

url = 'https://www.guokr.com/'
myHeaders = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'Cookie':'_ga=GA1.2.1694637488.1677082532; _gid=GA1.2.733826933.1677082532; _gat=1'
}
r = requests.get(url,headers=myHeaders)
#实例化
doc = pq(r.text)
# print('doc_html:\n',doc)
#第二个标签
lis = doc('ul.Nav__StyledNav-sc-186j2ft-0 li a').items()
for i in lis:
    print(i.text(),i.attr('href'))

