import pandas as pd
import requests
from bs4 import BeautifulSoup
url = 'https://www.zhihu.com/api/v4/topics/20021059/feeds/essence?offset=1&liit=10'
# url = 'http://www.tianqihoubao.com/aqi/beijing-202212.html'
headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
result = requests.get(url, headers=headers) #返回值是列表

# requestContent[0].to_csv('北京2020天气预报.csv',encoding='utf-8-sig',index=False)#
html=result.text
print(html)
soup = BeautifulSoup(result.text, 'lxml')