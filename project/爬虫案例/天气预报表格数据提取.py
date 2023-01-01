'''
快速批量抓取表格数据并保存
1.re
2.xpath
3.BeautifulSoup

天气预报地址
url = 'http://www.tianqihoubao.com/aqi/beijing-202012.html'

pandas:数据分析库：数据清洗，处理，下载，下载的格式是表格
1. DataFrame 数据类型 村塾为表格
2 IO功能 read_html


抓取的表头会乱码，得就改，需要同意语言为英语，指定编码格式
直接去谷歌浏览器-审查元素-网络-找到请求的地址-点击-标头-响应标头-Content-Type: text/html; charset=gb2312,复制gb2312到Python代码
encoding='gb2312，这样终端打印就不会乱码了，
header=0第一行是表头不是数据

一般是utf-8,
gb一般是中国人开发的网站

页面表格数据必须是写在table中(指写网站的前端)
有的开发不走寻常路，用li ul写，倒是Python下pandas读取不出来
'''


import pandas as pd
url = 'http://www.tianqihoubao.com/aqi/beijing-202011.html'
# url = 'http://www.tianqihoubao.com/aqi/beijing-202212.html'
headers = {
     'User-Agent':'Chrome/108.0.0.0'
}
requestContent = pd.read_html(url,encoding='gb2312',header=0) #返回值是列表

requestContent[0].to_csv('北京2020天气预报.csv',encoding='utf-8-sig',index=False)#1保存为csv格式，可以记事本和表格打开
#requestContent.to_excel('天气预报1.xlsx')#2保存为xlsx格式，可以记事本和表格打开

#3代码保存形式
# m8 = pd.DataFrame(requestContent)#抓取表格数据
# print(requestContent)
#
# m8.to_excel('天气预报.xlsx',index=0)

#执行代码时要调用函数---下载多个数据
#定义个函数，参数是地址url，和文件名字file_name
def get_table(url,file_name):
     print('下载成功')
     df_list=pd.read_html(url,encoding='gb2312',header=0)
     df_list[0].to_csv(file_name,encoding='utf-8-sig',index=False)
#变换城市名字和时间就可以下载任何城市的数据
cities=['beijing','wuhan']
# months=['202001','202002']
#列表推导时来写月份
'''
2020%02d:字符串格式化
1-12
生成数字，从202001到202012
'''
#采集北京 武汉从1到12月的数据
monthes=['2020%02d' %num for num in range(1,13)]
print('月份' + str(monthes))
for city in cities:
     for month in monthes:
          url = f'http://www.tianqihoubao.com/aqi/{city}-{month}.html' #前面加fr-相对路径
          # file_name = f'{city}-{month}.csv' #放到项目路径下
          #放到执行路径下--绝对路径

          file_name = fr'/Users/zoujunping/python采集资源/爬取天气预报/{city}-{month}.csv'
          get_table(url,file_name) #下载多个数据，时间有点久，需要30秒吧，


