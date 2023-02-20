
'''
多行注释
猿急送接单:
https://www.yuanjisong.com/job/allcity/page10

import pandas as pd
pandas爬虫工具
取名为pd

大学排名网址: https://www.dxsbb.com/news/64977.html

接单网站:

https://codemart.com/ 码市 兼职

https://zb.oschina.net/开源众包

https://www.taskcity.com/ 智城外包网
对于想创业的朋友，自己在开公司的，自己引流，运营都比较好做的

'''
from pathlib import Path

# 1需要接触一个工具
import pandas as pd
import openpyxl
import requests
import  ssl

#外链的网页爬不到css
ssl._create_default_https_context = ssl._create_unverified_context
# 2 拿到要爬取的网址
#  网址 = 'https://www.dxsbb.com/news/64977.html'

#网站404被删除

requestURL = 'https://www.dxsbb.com/news/42717.html'
# 3 需要通过工具爬取到我想要的内容
requestContent = pd.read_html(requestURL)[0]
m8 = pd.DataFrame(requestContent)
'''
保存后缀为xlsx可以用，但是这方法已经被Pandas放弃，虽然也可以用
print(requestContent)
m8.to_excel('爬虫兼职.xls',index=0)
'''
# data_folder = Path("代码run后保存路径")
m8.to_excel('/Users/zoujunping/Python/代码run后保存路径/爬虫兼职1.xls',engine='openpyxl')

#to_excel('路径')
#to_excel(r'路径') 加r保存的文件夹则红色


'''
加index=0,是为了区分表格不会乱爬，因为表格是有01 02 03之类的表格
'''
# 6


