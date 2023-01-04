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
jieba.setLogLevel(jieba.logging.INFO)

answers = []

kArr = []
# url1 =  f'https://www.zhihu.com/topic/20021059/hot?offset={offset}&liit=10'
# jieba.analyse.extract_tags(sentence,topK=20,withWeight=False,allowPOS=())

# with open(r'./answers.txt','w',encoding='UTF-8') as f:
# class demo:
#     def __init__(self):
result = {}
with open(r'/Users/zoujunping/python采集资源/豆瓣排行榜/news.html','w',encoding='UTF-8') as f:
    offset = 0
    while True:
        url = f'https://www.zhihu.com/api/v4/topics/20021059/feeds/essence?offset={offset}&liit=10'
        r = requests.get(url,headers=headers)
        info = r.json()

        if 'error' in info:
            msg = info['error']['message']
            print(f'任务中断,错误信息为:{msg}')
            break
        if info['paging']['is_end']:
            print('任务搞定')
            break
        for answer in info['data']:
            if answer['target']['type'] != 'answer':
                continue

            content = answer['target']['content']
            answers.append(content)


            f.write(json.dumps(answers, ensure_ascii=False))
            f.write('\n')
        # print('数组长度:' + str(len(answers)))
        # print(len(answer))
            offset += 0
            time.sleep(3)
            print('数组长度:' + str(len(answers)))
                #提取关键词及绘制词云
            for answer_index in answers:
                # print('水果王子:' + str(answer_index))
                clean_answer = BeautifulSoup(answer_index,'lxml').text
                # print('Apple' + clean_answer)
                kArr += jieba.analyse.extract_tags(clean_answer,withWeight=True)
                # jieba.setLogLevel(jieba.loggging.Info)
                # print(answer_index)
                # for i in kArr:
                #     #打印提取的数据
                #     print(i)


                for key,value in kArr:
                    if key not in result:
                        result[key] = value
                    else:
                        result[key] += value

                #倒序排序
                result = dict(sorted(result.items(),key=lambda result:result[1],reverse=False))
                print(result)
                jieba.load_userdict('news.html')
                jieba.analyse.set_stop_words('stop_words.html')
                # for v in result.values():
                #     print('values = {}'.format(v))
                # jieba.load_userdict('new.html')
                #打印Key
                # for k in result.keys():
                #     print('key={}'.format(k))
            # for i in kArr:
            #     print(i)
        # print(len(kArr))


    print('执行结束')
    # __init__()
