import time
import json
import requests
import pandas as pd

url = r'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
html = requests.get(url)
html.json() #将json转化成dict形式
data = json.loads(html.json()['data'])
china_data = data['areaTree'][0]['children']
data_set = []

for i in china_data:
    data_dict = {}
    data_dict['province'] = i['name']
    data_dict['nowConfirm'] = i['total']['nowConfirm']
    data_dict['confirm'] = i['total']['confirm']
    data_dict['dead'] = i['total']['dead']
    data_dict['heal'] = i['total']['heal']
    data_dict['deadRate'] = i['total']['deadRate']
    data_dict['healRate'] = i['total']['healRate']

    data_set.append(data_dict)


df = pd.DataFrame(data_set)#生成dataframe数据 （类似表格数据）
df.to_csv('epidemic_data.csv') #保存到本地的csv数据

# 数据可视化 matplotlib pyecharts（好看）

from pyecharts import options as opts
from pyecharts.charts import Bar, Line, Pie, Grid, Map
df2 = df.sort_values(by = ['nowConfirm'], ascending=False)[:5]
print(df2)
#将dateframe转换成list
df2 = [list(i) for i in zip(df2['province'].values.tolist(), df2['nowConfirm'].values.tolist())]

#画饼图并保存html文件至当前目录
pie = (
    Pie()
    .add(
        "",
        df2,
        radius=["10%", "30%"]
    )
    .set_global_opts(
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="70%", pos_left="70%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
)

pie.render()#保存html文件至当前目录


china_map = (
    Map()
    .add("现有确诊", df2)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="各地区确诊人数", pos_top="48%", pos_left="65%"),
        visualmap_opts=opts.VisualMapOpts(max_=200, is_piecewise=True),
        legend_opts=opts.LegendOpts(pos_left="90%", pos_top="60%")
    )
)
china_map.render('china_map.html')
