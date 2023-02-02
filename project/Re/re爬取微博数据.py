from bs4 import BeautifulSoup
import requests
import re


url = "https://s.weibo.com/weibo?q=%E8%87%B4%E5%B8%82%E6%B0%91%E7%9A%84%E4%B8%80%E5%B0%81%E4%BF%A1"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
# response = requests.get(url,headers = headers)
# if response.status_code!=200:
#    return

key = "致市民的一封信"  # input("请输入爬取关键字:")
for page in range(1, 2):
    params = (
        ('containerid', f'100103type=1&q={key}'),
        ('page_type', 'searchall'),
        ('page', str(page)),
    )

    response = requests.get('https://m.weibo.cn/api/container/getIndex', headers=headers, params=params)

    html = response.text


    #爬取整个网页
    soup = BeautifulSoup(html,'lxml')
    print(type(html),len(html))

    with open("page"+str(page).replace('/', '_') + ".html", "wb") as f:
        # 写文件用bytes而不是str，所以要转码
        f.write(html.encode('utf-8'))
    div = soup.find_all('div',class_="card-wrap")
    print(div,type(div))
    p = soup.find_all('p',class_="txt")
    print(len(p),type(p),"p")


#寻找html元素
    r = response.text
    title = re.findall('"page_title":"(.*?)"', r)
    content1 = re.findall('"content1":"(.*?)"', r)
    comments_count = re.findall('"comments_count":(.*?),', r)
    attitudes_count = re.findall('"attitudes_count":(.*?),', r)
    created_at = re.findall('"created_at":(.*?),', r)
    print('时间:\n',created_at)
    screen_name = re.findall('"screen_name":(.*?),', r)
    print('标题:\n', screen_name)
    for i in range(len(title)):
        print(eval(f"'{title[i]}'"),screen_name[i])
        print(eval(f"'{content1[i]}'"), comments_count[i], attitudes_count[i])


'''
变量名
title 中国笔架山岛申遗——致市民朋友们的一封信
created_at "Tue Dec 27 21:17:51 +0800 2022"
screen_name "爱世界遗产"
title #三亚倡议市民游客非必要不做核酸#
created_at "Wed Dec 21 09:14:15 +0800 2022"
screen_name "新京报"

'''





'''
获取日期与时间
# date = r'\d{4}-\d{2}-\d{2}'
# date_title=re.findall(date,r)
# print('日期', date_title)
#
# time = r'\d{1,2}(?:(?:am|pm)|(?::\d{1,2})(?:am|pm)?)'
# time_title = re.findall(time, r)
# print("日期时间:\n", time_title)
#
# res = r'<a .*?>(.*?)</a>'
# # texts = re.findall(res, content, re.S | re.M)
#
# timer_title = re.findall(date, r, re.S | re.M)
# print('xxxxxxxxxxxxxxxx', timer_title)
# #打印index值
# for t in timer_title:
#     print(t)


'''