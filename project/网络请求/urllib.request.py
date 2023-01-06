#
# '''
# urllib.request没有requests好用
#
# '''
# import urllib.request
# url1 = 'http://www.baidu.com'
# # url1 = "http://www.zueb.edu.cn/site/xsgate/xsyw/index.html" #出错
# print(url1)
# # 打开网页
# rep = urllib.request.urlopen(url1)
# # 获取网页内容
# try:
#     html =  rep.read()
#     print('网页',html)
# except:
#     print("出错了！")
