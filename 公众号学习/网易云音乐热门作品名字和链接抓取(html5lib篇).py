#使用html5lib方法来实现的代码，简单来说就是用html5lib修复html就可以了

import requests, re
from lxml import etree
from fake_useragent import UserAgent
import html5lib
# 网易云音乐热门作品名字和链接抓取(pyquery篇)，行之有效，难点在于构造pyquery选择器

class Wangyiyun(object):
    def __init__(self):
        self.base_url = 'https://music.163.com/discover/artist'
        self.headers = {
            'user-agent': UserAgent().random,
            'referer': 'https://music.163.com/',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
        }

    def get_xpath(self, url):
        res = requests.get(url, headers=self.headers)
        # print(res.text)
        # return etree.HTML(etree.tostring(html5lib.parse(res.text, treebuilder='lxml')))
        return etree.HTML(etree.tostring(html5lib.parse(res.text, treebuilder='lxml'), encoding='iso8859-1'))

    def singers_parse(self, url, items):
        html = self.get_xpath(url)
        song_dict = {}
        a_lis = html.xpath('//div[@id="song-list-pre-cache"]/ul/li/a')  # "song-list-pre-cache"
        for a in a_lis:
            song_name = a.xpath('.//text()')[0]
            print(song_name)
            song_url = 'https://music.163.com' + a.xpath('./@href')[0]
            print(song_url)
            # song_dict[song_name] = song_url
        items['所有歌曲：'] = song_dict
        # print(items)
        # name = items['歌手名：']
        # print(f'歌手：{name} 的歌曲已经获取完毕！即将写入文件！')
        # time.sleep(1)
        # self.writer_data(items)
        # print(f'歌手：{name} 的歌曲已经写入完毕！')


Wangyiyun().singers_parse(url='https://music.163.com/artist?id=50653540', items={})

# 目前我们已经实现了使用正则表达式、xpath和bs4和pyquery四种方法来进行操作，接下来的一篇文章，我们html5lib库来进行实现