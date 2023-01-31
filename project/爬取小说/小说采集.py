
import requests
import time
from bs4 import BeautifulSoup
import random
from random import randint
# 小说获取
def display(headers):
    headers={
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44'
    }

    session = requests.session()
    url = 'https://www.biquge.tv/7_7365/'
    # //https: // www.qbiqu.com / 7_7365 /
    while(1):
        try:
            page_text=session.get(url=url, headers=headers)
            break
        except Exception as e:
            print(e)
            time.leep(2)
            page_text=page_text.encode('iso-8859-1').decode(page_text.apparent_encoding)
            soup=BeautifulSoup(page_text, 'lxml')
            dd_list = soup.select('.cover  > .chapter > li')
            fp = open('/Users/zoujunping/python采集资源/小说采集01/fanrenxiuxian.txt', 'w', encoding='utf-8')
            flag = 1
            for dd in dd_list:
                title=dd.a.string
                detail_url = 'https://www.qbiqu.com/' + dd.a["href"]
                try:
                    detail_page_text = session.get(url=detail_url, headers=headers)
                    detail_page_text = detail_page_text.text.encode('iso-8859-1').decode(detail_page_text.apparent_encoding)
                    detail_soup = BeautifulSoup(detail_page_text, 'lxml')
                    div_tag = detail_soup.find('div', id='content')
                    content = div_tag.text  # .split("&nbsp;&nbsp;&nbsp;&nbsp;")
                    fp.write(title + ":" + content + "\n")
                    print(title, "爬取成功")
                    time.sleep(3)
                    break
                except Exception as e:
                    print(e)




















