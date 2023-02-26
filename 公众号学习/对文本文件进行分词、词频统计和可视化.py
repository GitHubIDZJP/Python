import re
import collections  # 词频统计库
import numpy as np  # numpy数据处理库
import jieba  # 结巴分词
jieba.setLogLevel(jieba.logging.INFO)
import requests
from bs4 import BeautifulSoup

from pyecharts import options as opts
from pyecharts.charts import WordCloud
from pyecharts.globals import SymbolType

import warnings

warnings.filterwarnings('ignore')

r = requests.get("https://m.thepaper.cn/baijiahao_11694997", timeout=10)
r.encoding = "utf-8"
s = BeautifulSoup(r.text, "html.parser")
f = open("报告.txt", "w", encoding="utf-8")
L = s.find_all("p")
for c in L:
    f.write("{}\n".format(c.text))

f.close()
fn = open("./报告.txt","r",encoding="utf-8")
string_data = fn.read()
fn.close()
# 文本预处理
# 定义正则表达式匹配模式
pattern = re.compile(u'\t|,|/|。|\n|\.|-|:|;|\)|\(|\?|"')
string_data = re.sub(pattern,'',string_data)  # 将符合模式的字符去除
# 文本分词
# 精确模式分词
seg_list_exact = jieba.cut(string_data,cut_all=False)
object_list = []
# 自定义去除词库
remove_words = [u'的',u'要', u'“',u'”',u'和',u'，',u'为',u'是',
                '以' u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',
                u' ',u'、',u'中',u'在',u'了',u'通常',u'如果',u'我',
                u'她',u'（',u'）',u'他',u'你',u'？',u'—',u'就',
                u'着',u'说',u'上',u'这', u'那',u'有', u'也',
                u'什么', u'·', u'将', u'没有', u'到', u'不', u'去']

for word in seg_list_exact:
    if word not in remove_words:
        object_list.append(word)
# 词频统计
# 对分词做词频统计
word_counts = collections.Counter(object_list)
# 获取前30最高频的词
word_counts_all = word_counts.most_common()
word_counts_top30 = word_counts.most_common(30)
print("2021年政府工作报告一共有%d个词"%len(word_counts))
print(word_counts_top30)

import pyecharts
from pyecharts.charts import Line
from pyecharts import options as opts

# 示例数据
cate = [i[0] for i in word_counts_top30]
data1 = [i[1] for i in word_counts_top30]

line = (Line()
       .add_xaxis(cate)
       .add_yaxis('词频', data1,
                  markline_opts=opts.MarkLineOpts(data=[opts.MarkLineItem(type_="average")]))
       .set_global_opts(title_opts=opts.TitleOpts(title="词频统计Top30", subtitle=""),
       xaxis_opts=opts.AxisOpts(name_rotate=60,axislabel_opts={"rotate":45}))
      )

line.render_notebook()