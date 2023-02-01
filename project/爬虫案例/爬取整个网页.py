import urllib.request

import  ssl

#外链的网页爬不到css
ssl._create_default_https_context = ssl._create_unverified_context
def baiduNet():
    url = "http://zw.hainan.gov.cn/wssc/emalls.html"
    response = urllib.request.urlopen(url).read().decode('utf-8')
    file = open("baidutext.html", "w")
    file.write(response)
if __name__ == "__main__":
    baiduNet()
