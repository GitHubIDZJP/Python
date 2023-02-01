# 使用 urllib
import requests
# 使用 lxml
from lxml import etree
from  bs4 import  BeautifulSoup
# 定义 header
headers = {
  # UA 最基本的防爬识别
  'User-Agent': 'Mozilla/5.0 (X11; Linux aarch64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.188 Safari/537.36 CrKey/1.54.250320'
}

# 1、定义一个 https 的 url
url = 'https://s.weibo.com/weibo?q=%E8%87%B4%E5%B8%82%E6%B0%91%E7%9A%84%E4%B8%80%E5%B0%81%E4%BF%A1'
#2
result = requests.get(url, headers=headers)  # HTTP GET POST PUT
print(result.status_code)
html = result.text
soup=BeautifulSoup(html,'lxml')
soup=BeautifulSoup(html,'lxml')
ranking = soup.find_all('p',class_='txt')
for j in ranking:
  rank = ranking[j].find('p').text if ranking[j].find('p') else 0
  print(rank)


















