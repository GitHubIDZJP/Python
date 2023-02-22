import requests
from lxml import etree
import time
def getArticle(url):
    global data
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    # get 请求
    r = requests.get(url, headers=headers)
    # 提取数据
    html = etree.HTML(r.text)
    article = html.xpath(
        '//h1/text() | //p[@class="article_author"]/span/text() | //div[@class="article_text"]/p/text()'
    )
    # 追加的方式写到文本文件中
    data = '''
%s  %s  %s  %s  %s  %s  %s  %s
                    '''%(str(time.ctime()),'\n\n《',str(article[0]),'》','\n\n作者：', str(article[1]), '\n\n',str('\n'.join(article[2:])))
    with open('article.txt', 'w', encoding='utf-8') as f:
        f.write(time.ctime() + '\n\n《' + article[0] + '》' + '\n\n作者：' + article[1] + '\n\n')
        f.write('\n'.join(article[2:]))
        f.write('\n\n')
        print(data)
    return data

if __name__ == '__main__':
    url = 'https://meiriyiwen.com'
    data = getArticle(url)
    print("获取数据:\n",data)