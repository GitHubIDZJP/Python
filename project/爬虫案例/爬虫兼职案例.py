
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


# 1需要接触一个工具
import pandas as pd
import requests
# 2 拿到要爬取的网址
#  网址 = 'https://www.dxsbb.com/news/64977.html'
requestURL = 'https://www.dxsbb.com/news/64977.html'
# requestURL = 'https://www.dxsbb.com/news/42717.html'
# 3 需要通过工具爬取到我想要的内容
requestContent = pd.read_html(requestURL)[0]
m8 = pd.DataFrame(requestContent)
# 4 打印爬取的数据
print(requestContent)
# 5 把数据保存到电子表格里
m8.to_excel('爬虫兼职.xlsx',index=0)
# requestContent.to_execel('爬虫兼职.xlsx',index=0)
'''
加index=0,是为了区分表格不会乱爬，因为表格是有01 02 03之类的表格
'''
# 6


