import requests

def getHtml(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return  r.text
    except:
        return '异常'
# if __name__='__main__': 错误
if __name__ == "__main__":
    url1 = "http://www.zueb.edu.cn/site/xsgate/xsyw/index.html"
    getHtml(url1)