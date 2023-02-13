'''
爬取指定关键字图片
'''
import re  # 正则表达式，解析网页
import requests  # 请求网页
import traceback
import os


def dowmloadPic(html, keyword, startNum):
    headers = {'user-agent': 'Mozilla/5.0'}  # 浏览器伪装，因为有的网站会反爬虫，通过该headers可以伪装成浏览器访问，否则user-agent中的代理信息为python
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 找到符合正则规则的目标网站
    num = len(pic_url)
    i = startNum
    subroot = root + '/' + word
    txtpath = subroot + '/download_detail.txt'

    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')

    for each in pic_url:
        a = '第' + str(i + 1) + '张图片，图片地址:' + str(each) + '\n'
        b = '正在下载' + a
        print(b)
        path = subroot + '/' + str(i + 1)
        try:
            if not os.path.exists(subroot):
                os.mkdir(subroot)
            if not os.path.exists(path):
                pic = requests.get(each, headers=headers, timeout=10)
                with open(path + '.jpg', 'wb') as f:
                    f.write(pic.content)
                    f.close()
                with open(txtpath, 'a') as f:
                    f.write(a)
                    f.close()

        except:
            traceback.print_exc()
            print('【错误】当前图片无法下载')
            continue
        i += 1

    return i


if __name__ == '__main__':

    headers = {'user-agent': 'Mozilla/5.0'}
    words = input('您要爬取什么图片:')
    # words = ['桃子', '苹果', '梨']
    # words为一个列表，可以自动保存多个关键字的图片
    root = './download_images_of_'
    for word in words:
        root = root + word + '&'
    if not os.path.exists(root):
        os.mkdir(root)
    for word in words:
        lastNum = 0
        # word = input("Input key word: ")
        if word.strip() == "exit":
            break
        pageId = 0
        # 此处的参数为需爬取的页数，设置为2页
        for i in range(3):
            url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + "&pn=" + str(
                pageId) + "&gsm=?&ct=&ic=0&lm=-1&width=0&height=0"
            pageId += 20  # 好像没啥影响
            html = requests.get(url, headers=headers)
            # print(html.text) #打印网页源码，相当于在网页中右键查看源码内容
            lastNum = dowmloadPic(html.text, word, lastNum, )  # 本条语句执行一次获取60张图

