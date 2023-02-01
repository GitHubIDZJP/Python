#re提取、匹配、替换
headers = {
  # UA 最基本的防爬识别
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}
# url = 'https://read.douban.com/provider/all'
# # result = requests.get(url, headers=headers)  # HTTP GET POST PUT
import re
import urllib.request
import  ssl

# context = ssl.create_default_context()
ssl._create_default_https_context = ssl._create_unverified_context

openhead=urllib.request.build_opener()
openhead.addheaders = [("User-Agent", "Chrome/88.0.4324.188")]
urllib.request.install_opener(openhead)
url_douban = "https://read.douban.com/provider/all"
url_blog = "http://www.eastmountyxz.com/"
resuest = urllib.request.urlopen(url_blog).read().decode('utf-8')
#模板


res = 'a href="(.*?)"'
fetchContent = re.findall(res,resuest,re.I)
print('***:' + str(fetchContent))

# #打印:
# # for url in urls:
# #     print(url)
#
title = re.findall(r'<a>(.*)</a>', resuest,re.S|re.M)
print('***网页标题:***\n',title)
#
#
#
# #提取div下img图片链接
# s = 'img src="(.*?)"'
# fetch_img = re.findall(s, resuest, re.S )
# for img in fetch_img:
#     print('提取图片:\n',img)
#
# # 提取字母
# letter = r'<div class="index-name">(.*?)</div>'
# fetch_letter = re.findall(letter,resuest,re.I)
# print('***:' + str(fetch_letter))