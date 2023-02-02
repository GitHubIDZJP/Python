from bs4 import BeautifulSoup
import requests
# 模拟浏览器
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
url = 'http://www.eastmountyxz.com/'

# myHeaders = {
#     'User-Agent':'Chrome/108.0.0.0'
# }



# 打印网页源代码-HTML
# print(result.text)
# html=result.text

# soup=BeautifulSoup(html,'lxml')






result = requests.get(url, headers=headers)  # HTTP GET POST PUT
print(result.status_code)
result.encoding = 'utf-8'
soup = BeautifulSoup(result.text,'lxml')
dataArr = soup.findAll('div',class_='essay')
for i  in dataArr:
    title = i.find('h1').text.strip()
    print(title)
    content = i.find('p').text.strip()
    print(content)
# soup = BeautifulSoup(resuest)
# for i in range(0,10):
#     if(i == 0):
#         title = soup.find_all("div",class_="essay")
#     else:
#         title = soup.find_all("div",class_="essay"+str(i))
#     for t in title:
#         print('***网页标题:***\n',t.getText())