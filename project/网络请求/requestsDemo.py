import requests
url = 'http://graph.nodes-link.com/'
# url = 'https://baidu.com'
myHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
result=requests.get(url,headers=myHeaders)

# print(result.content)
print(result.text)
print('----------------------------')
print('sdsd')
with open(r'/Users/zoujunping/python采集资源/豆瓣排行榜/index.html','wb') as f:
    f.write(result.content)
    print('保存成功 ! ! !')