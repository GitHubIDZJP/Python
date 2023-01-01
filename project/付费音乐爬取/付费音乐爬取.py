import  requests  #网络请求类 第三方 pip install 类名
import json   # 数据格式类库 通用数据格式
'''
1 程序的架构形式
 c/s 架构形式 client 客户端 server 服务端 游戏
 b/s browser 浏览器
 
 2 b/s架构访问过程
   http协议 ---> TCP/IP
   request 请求
   response 响应
   
  解码网址 url =  http://www.kuwo.cn/search/list?key=%E5%BC%A0%E5%AD%A6%E5%8F%8B
3 网址: 
  进入酷我音乐网站，输入歌手张学友
  点击第一个http://www.kuwo.cn/search/list?key=%E5%BC%A0%E5%AD%A6%E5%8F%8B(被加密)，去解密
  解密请求头:http://www.kuwo.cn/search/list?key=%E5%BC%A0%E5%AD%A6%E5%8F%8B
  解密网站:https://tool.chinaz.com/tools/urlencode.aspx -- url编码/解码
  把要解码的网站url输入后点UrlDecode解码显示为http://www.kuwo.cn/search/list?key=张学友(解码后网址)
  解码前%E5%BC%A0%E5%AD%A6%E5%8F%8B
  解码后:张学友
  
  远程地址：127.0.0.1:15732(服务器IP地址)
  
  请求标头(Request Headers):
  我们向别人服务器发送请求的时候，必须携带的一些信息:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=张学友&pn=1&rn=30&httpsStatus=1&reqId=a8ac74d0-8965-11ed-9323-d778ff910184'
url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key=张学友&pn=1&rn=30&httpsStatus=1&reqId=a8ac74d0-8965-11ed-9323-d778ff910184'

json数据格式化网站:
      https://www.bejson.com/jsonviewernew/

kw_token=U8F6Z99PHGR; path=/; expires=Mon, 30 Jan 2023 23:48:43 GMT
Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1672530307; _ga=GA1.2.271550435.1672530308; _gid=GA1.2.1793260520.1672530308; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1672530424; kw_token=U8F6Z99PHGR
Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1672530307; _ga=GA1.2.271550435.1672530308; _gid=GA1.2.1793260520.1672530308; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1672530424; kw_token=U8F6Z99PHGR

'''

#请求头--HTTP协议
headers = {
    #用户代理
    # 'User-Agent':'Chrome/108.0.0.0'
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    #需要的链接,需要单引号隔开，因为是字典形式
    'Referer':'http://www.kuwo.cn/search/list?key=%E5%BC%A0%E5%AD%A6%E5%8F%8B',

    #会员独一五一的标识。如没有这个则爬不了会员数据
    'csrf':'RUJ53PGJ4ZD',
    # 'csrf':'N32JILBCZGB',
    #会员的cokkie ,如果是非会员，则爬取不了
    'Cookie':'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1672530307; _ga=GA1.2.271550435.1672530308; _gid=GA1.2.1793260520.1672530308; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1672530424; kw_token=U8F6Z99PHGR'
}
# 跟用户输入想爬取的歌曲
singer = input('请输入歌手名:')
page = int(input('请输入下载页数:'))
# 逻辑思维-做事得理解流程
url = 'http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn=1&rn=30&httpsStatus=1&reqId=a8ac74d0-8965-11ed-9323-d778ff910184'
#访问服务器
response = requests.get(url,headers=headers)
print(response.text)
#把数据转为JSON
result = json.loads(response.text)
#提取数据
data  = result['data']['list']

#从data提取 rid name
for  song_info in data:
    # 取得rid
    rid = song_info['rid']
    #提取歌曲名字
    name = song_info['name']
    #通过哪个链接去访问服务器--这个地址是错的
    url = 'http://www.kuwo.cn/api/www/search/searchKey?key=&httpsStatus=1&reqId=19d6b820-8973-11ed-9cb5-e1133980b9aa'
    #获取资源地址
    res = requests.get(url,headers).json()
    #把歌曲URL提取
    music_url = res['url']
    #文件i/o读写下载
    with open('我的音乐/{}.mp3'.format(name),'wb') as f:
        print('正在下载{}'.format(name),end='')
        music = requests.get(music_url)
        f.write(music.content)
        f.close()
        print('')





