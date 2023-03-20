import csv

import requests
from bs4 import BeautifulSoup as bs
from lxml import etree


def get_page_url(url):
    try:
        global url1
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
        html = requests.get(url,headers=headers).text
        # bs4解析
        soup = bs(html, 'lxml')
        lu = soup.find('div',class_='list clearfix')
        hrefs = lu.find_all('a')
        # print(hrefs)
        # 获取二级页面的详情页url
        url_list = []
        for k in hrefs[:6]:
            urls = url1 + k['href']
            url_list.append(urls)
        return url_list

        # xpath 解析失败
        # tree = etree.HTML(html)
        # a_list = tree.xpath('/html/body/div[7]/div[1]/wbfwrap/div/div[2]/a[1]/text()')
        # print(a_list)

    except:
        print("请求异常！")


# 请求分析乡情页面
def get_page_info(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36"}
    html = requests.get(url, headers=headers).text
    soup = bs(html,'lxml')
    h1 = soup.find_all('h1',class_="title")
    # 公家路线
    bus_name = h1[0].span.string
    # 线路性质
    bus_type = h1[0].a.string
    # 运行时间
    h2 = soup.find_all('ul',class_="bus-desc")
    bus_time = h2[0].li.string
    # 参考票价
    ticket = h2[0].li.next_sibling.string
    print(ticket)
    # 公司信息
    gongsi = h2[0].find_all('a')[0].string
    print(gongsi)
    # 最后更新
    h3 = h2[0].li.next_sibling.next_sibling.next_sibling
    gengxin = h3.find('span',tabindex="0").string
    # print(h3)
    print(gengxin)
    try:
        wang_info = soup.find_all('div',class_="trip")[0].string
        print(wang_info)
    except:
        wang_info = None
    try:
        fan_info = soup.find_all('div',class_="trip")[1].string
        print(fan_info)
    except:
        fan_info = None
    try:
        wang_list_tag = soup.find_all('div',class_="bus-lzlist mb15")[0].find_all('a')
    except:
        wang_list_tag = None
    try:
        fan_list_tag = soup.find_all('div',class_="bus-lzlist mb15")[1].find_all('a')
    except:
        fan_list_tag = None
    # fan_list_tag = None
    wang_buff = ""
    fan_buff = ""
    for wang in wang_list_tag:
        wang_buff += wang.string+','
    print(wang_buff)
    if fan_list_tag:
        for fan in fan_list_tag:
            fan_buff += fan.string+','
    print(fan_buff)
    result_list = [bus_name,bus_type,bus_time,gongsi,gengxin,wang_info,wang_buff,fan_info,fan_buff]
    # result2_list = []
    dic = {'bus_name':None,'bus_type':None,'bus_time':None,'gongsi':None,'gengxin':None,'wang_info':None,'wang_buff':None,'fan_info':None,'fan_buff':None}
    count = 0
    for k in dic.keys():
        dic[k] = result_list[count]
        count += 1
        # else:
        #     result2_list.append(None)
    # print(result2_list)
    print(dic)
    lst = []
    lst.append(dic)
    with open('chengdu_bus_info.csv','a+',encoding='utf-8',newline='') as fp:
        writer = csv.DictWriter(fp, fieldnames=header)
        writer.writerows(lst)


    # bus_name = bs(h1.text,'lxml')
    # bus_name = bus_name.select('html>body>p')[0].string
    # bus_type = soup
    # print(bus_name)


if __name__ == '__main__':
    header = ['bus_name','bus_type','bus_time','gongsi','gengxin','wang_info','wang_buff','fan_info','fan_buff']
    with open('bus_info.csv', 'w', encoding='utf-8',newline="") as fp:
        writer = csv.DictWriter(fp,fieldnames=header)
        writer.writeheader()
    # 遍历得出每个一级页面的url
    url1 = "https://chengdu.8684.cn/"
    url_list = url1 + "/list{}"
    for i in range(1,10):
        url = url_list.format(i)
        print(url)
        a = get_page_url(url)
        for i in a:
            get_page_info(i)