import json

import  requests
import  time
import json
from bs4 import BeautifulSoup
import jieba.analyse
import re
import  csv
import pandas as pd
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
answers = []
offset = 0
k = []
# url1 =  f'https://www.zhihu.com/topic/20021059/hot?offset={offset}&liit=10'
# jieba.analyse.extract_tags(sentence,topK=20,withWeight=False,allowPOS=())
while True:
    # url1 = f'https://www.zhihu.com/topic/20021059/hot?offset={offset}&liit=10'
    url = f'https://www.zhihu.com/api/v4/topics/20021059/feeds/essence?offset={offset}&liit=10.html'
    # print(f'获取{url}...')
    # print(ur1)#https://www.zhihu.com/api/v4/topics/20021059/feeds/essence?offset=0&liit=10
    r = requests.get(url,headers=headers)
    info = r.json()
    # tree = etree.HTML(r.content.decode('utf-8'))

    # print(info)
    if 'error' in info:
        msg = info['error']['message']
        print(f'任务中断,错误信息为:{msg}')
        break
    if info['paging']['is_end']:
        print('任务搞定')
        break
    for answer in info['data']:
        # print(answer)
        # print(answer)
        print(len(answers))
        if answer['target']['type'] != 'answer':
            continue
            content = answer['target']['content']
            answer = f.write(json.dump(content))
            f.write('\n')
            # answers.append(answer)
            print(len(answer))
            # html = content
            # dr = html.
            # answers.append(content)
            # print(content)
            offset += 4
            time.sleep(4)

    for i in answers:
        c = BeautifulSoup(i, 'lxml').text
        dr = c
        k += jieba.analyse.extract_tags(c,withWeight=True)
        print(c)
        print('执行完毕')
    # for i in answers:
    #     print(i)
    # for i in answers:
    #     c = BeautifulSoup(i, 'lxml').text
    #     k += jieba.analyse.extract_tags(c,withWeight=True)
    #     print(k)

        # print(answers)
    # print(tree.xpath('//p/@value'))

        #

            # print(answers)
        # for a in answers:
        #     clean_answer = BeautifulSoup(a, 'lxml').text
        #     keyboards += jieba.analyse.extract_tags(clean_answer, withWeight=True)
        #     print(clean_answer)

            # for i in answers:
            #     print(i)
# for answer  in answers:
#     clean_a_b = BeautifulSoup(answer,'lxml').text
#     keyboards += jieba.analyse.extract_tags(clean_a_b,withWeight=True)
# print('说过王子:' + str(keyboards))
    # s = BeautifulSoup
