
'''

pip install quote

# http://api.qingyunke.com/api.php?key=free&appid=0&msg=  API地址
 智能机器人API： https://www.sojson.com/api/semantic.html
'''
import  urllib.request
from  urllib.parse import quote
import  string


def main():
    # 循环处理，客户端发送的聊天信息
    while True:
        # 定义一个url地址 格式为：API地址 + 用户聊天输入发送的语句内容
        url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg=' + input("请输入您要发送的消息")
        # urllib.request.urlopen不支持中英文混合的字符串。
        # 所以应使用urllib.parse.quote进行转换。
        # 方法quote的参数safe表示可以忽略的字符
        s = quote(url,safe=string.printable)
        # string.printable表示ASCII码第33～126号可打印字符
        # 其中第48～57号为0～9十个阿拉伯数字；65～90号为26个大写英文字母，97～122号为26个小写英文字母
        # 其余的是一些标点符号、运算符号等。
        # 所以必须设置这个safe参数

        # 使用urllib.request请求URL，获得一个响应

        with urllib.request.urlopen(s) as response:
            html = response.read()
            # 将获取到的响应内容进行解码，并将json字符串内容转换为python字典格式
            # 通过下标取到机器人回复的内容
            print(eval(html.decode('utf-8'))["content"])
if __name__=="__main__":
    main()
# if __name__ == "__main__":


''''


终端打印:

我: 请输入您要发送的消息12
机器人: 13
我: 请输入您要发送的消息34
机器人: “34”是啥意思？
提示文字: 请输入您要发送的消息

请输入您要发送的消息  输入了做爱
{face:88}闪了，你这么猥琐，跟你聊天会降低人品的
请输入您要发送的消息

'''

