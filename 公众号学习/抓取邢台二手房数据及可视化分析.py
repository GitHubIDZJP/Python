import requests

url = 'https://xa.lianjia.com/ershoufang/yanliangqu/'
response = requests.get(url)

if response.status_code == 200:
    html = response.text
    print(html)
else:
    print('网页获取失败')
