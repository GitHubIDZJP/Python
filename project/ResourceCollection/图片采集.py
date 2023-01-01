# def say():
#     print("Hello,World!")
import requests
from bs4 import BeautifulSoup
#下载第三方库设置代理且信任
# pip install lxml -i http://mirrors.aliyun.com/pypi/simple/ --trusted-host mirrors.aliyun.com

def display(headers):
# 正文爬图片内容

 headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"}
# url="https://www.dpm.org.cn/lights/royal.html"
 imgName = 0
 for page in range(1, 4):
    url = f"https://www.dpm.org.cn/lights/royal/p/{page}.html"
    response = requests.get(url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html,"lxml")
    content_all = soup.find_all(class_="pic")
    for content in content_all:
        imgContent = content.find(name="img")
        imgName = imgName + 1

        imgUrl = imgContent.attrs["src"]  # 一页网页中每个图片的链接
        imgResponse = requests.get(imgUrl)
        img = imgResponse.content

        # print(imgUrl)

        with open(f"/Users/zoujunping/python采集资源/图片采集02/{imgName}.jpg", "wb") as f:
            f.write(img)



