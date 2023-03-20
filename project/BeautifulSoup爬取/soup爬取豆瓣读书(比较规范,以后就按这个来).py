# 豆瓣读书
import os
import csv
import random
from time import sleep
from fake_useragent import UserAgent
import requests
from bs4 import BeautifulSoup
def def_url(page):
    # 随机usera-gent，防止被封
    ua = UserAgent()
    head = ua.chrome
    header = {
        "user-agent": head,
        'cookie': 'bid=eoK7vIT-Vgk; gr_user_id=2295df48-5aa9-4a94-90d3-ec98be19200a; __utmz=30149280.1679297581.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=81379588.1679297581.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D9D6C66A97236F9CA5A40B052E90646B0|2a945e96a1dab215757608b84e54e87b; __yadk_uid=srTAsoQwhuYTgfCgUxhqAcMutX7szv8l; dbcl2="206521062:GcF7sRE1z6A"; push_noty_num=0; push_doumail_num=0; __gads=ID=c67be8eade4deb7c-226e5fd5d9de007b:T=1679301341:RT=1679301341:S=ALNI_Ma5byHx4y3cFfcPttoTsGuiERWuYQ; __gpi=UID=00000bdc4b22d0d6:T=1679301341:RT=1679301341:S=ALNI_MYfT4Tx0fIMJN6JMArD7SbQDgqbBg; _ga=GA1.1.1157641442.1679297581; _ga_RXNMP372GL=GS1.1.1679301358.1.1.1679302525.60.0.0; ck=ajNI; _pk_ref.100001.3ac3=["","",1679318506,"https://www.baidu.com/link?url=UlzZS_7rY7PqmOBqhRdLXSsonQln-yKKhNR8ZDvABPiFs9yH4VXtVnWmgsS8fZXj&wd=&eqid=c98b2f7d000de9850000000564180c28"]; _pk_ses.100001.3ac3=*; __utma=30149280.1157641442.1679297581.1679297581.1679318506.2; __utmc=30149280; __utmt_douban=1; __utma=81379588.746970357.1679297581.1679297581.1679318506.2; __utmc=81379588; __utmt=1; __utmb=30149280.2.10.1679318506; __utmb=81379588.2.10.1679318506; _pk_id.100001.3ac3=f10cf2fa0f2a3aec.1679297581.2.1679318584.1679302488.'
    }
    url = f'https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&amp;p={page}'
    response = requests.get(url,headers=header)
    xml = BeautifulSoup(response.text,'html.parser')
    msg = xml.findAll('li',class_='media clearfix')
    # print(msg)
    #
    book_dict_list = [] #空数组
    for li in msg:
        # print(li)
        sleep(random.uniform(0, 2)) #限制了爬的速度，防止被封,随机时间防止ip被封
        h2_text = str(li.find(name='h2').text.strip())
        # print(h2_text)
        p1_desc = li.find(name='p', class_="subject-abstract color-gray").text.strip()
        # print(p1_desc)

        bookMsg = {"书名":h2_text,"书本描述":p1_desc}
        print(bookMsg)

        book_dict_list.append(bookMsg)

        # 数据存到本地(存到MySql数据库也行)--我这里暂时保存到本地(格式cvs)

        fo = open("news.csv", "w", newline='', encoding='utf-8')
        # 表头
        header = ["书名", "书本描述"]
        writer = csv.DictWriter(fo, header)
        # 写入表头
        writer.writeheader()
        # 将上一步的字典写入csv文件中
        writer.writerows(book_dict_list)
        fo.close()
    print('保存成功')









if __name__ == '__main__':
    for i in range(1,3):
        def_url(i)
        print('-----------第'+str(i)+'页数据--------')



#这下面的也一样，跟上面代码一样效果，但是没这么美观
# for page in range(1, 3):
#     # 随机usera-gent，防止被封
#     ua = UserAgent()
#     head = ua.chrome
#     url = f'https://book.douban.com/latest?subcat=%E5%85%A8%E9%83%A8&amp;p=1'
#
#     headers = {
#         # UA 最基本的防爬识别
#         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
#         # 'User-Agent': head,
#         'cookie':'bid=eoK7vIT-Vgk; gr_user_id=2295df48-5aa9-4a94-90d3-ec98be19200a; __utmz=30149280.1679297581.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=81379588.1679297581.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _vwo_uuid_v2=D9D6C66A97236F9CA5A40B052E90646B0|2a945e96a1dab215757608b84e54e87b; __yadk_uid=srTAsoQwhuYTgfCgUxhqAcMutX7szv8l; dbcl2="206521062:GcF7sRE1z6A"; push_noty_num=0; push_doumail_num=0; __gads=ID=c67be8eade4deb7c-226e5fd5d9de007b:T=1679301341:RT=1679301341:S=ALNI_Ma5byHx4y3cFfcPttoTsGuiERWuYQ; __gpi=UID=00000bdc4b22d0d6:T=1679301341:RT=1679301341:S=ALNI_MYfT4Tx0fIMJN6JMArD7SbQDgqbBg; _ga=GA1.1.1157641442.1679297581; _ga_RXNMP372GL=GS1.1.1679301358.1.1.1679302525.60.0.0; ck=ajNI; _pk_ref.100001.3ac3=["","",1679318506,"https://www.baidu.com/link?url=UlzZS_7rY7PqmOBqhRdLXSsonQln-yKKhNR8ZDvABPiFs9yH4VXtVnWmgsS8fZXj&wd=&eqid=c98b2f7d000de9850000000564180c28"]; _pk_ses.100001.3ac3=*; __utma=30149280.1157641442.1679297581.1679297581.1679318506.2; __utmc=30149280; __utmt_douban=1; __utma=81379588.746970357.1679297581.1679297581.1679318506.2; __utmc=81379588; __utmt=1; __utmb=30149280.2.10.1679318506; __utmb=81379588.2.10.1679318506; _pk_id.100001.3ac3=f10cf2fa0f2a3aec.1679297581.2.1679318584.1679302488.'
#     }
#
#     response = requests.get(url,headers=headers)
#     soup = BeautifulSoup(response.content, 'html.parser')
#
#     book_Arr = soup.findAll('li',class_='media clearfix')
#     # print(book_Arr)
#     print('数组长度:\n',len(book_Arr))
#     for li in book_Arr:
#         # 随机时间防止ip被封
#         # sleep(random.uniform(0, 2))
#         h2 = str(li.find(name='h2').text.strip())
#         # print(h2)
#         p1_desc = li.find(name='p',class_="subject-abstract color-gray")
#         print(p1_desc.text.strip())
#


# 一页20本书msg，500/20=25