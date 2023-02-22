# http://www.xinfadi.com.cn/priceDetail.html

from playwright.sync_api import Playwright, sync_playwright
import datetime
from pprint import pprint
import traceback
import logging
from tqdm import tqdm
import json

# pip install playwright，然后终端 playwright install
"""
先用playwright写一个普通的登入网站代码，然后page.goto前面加上
page.on("request", lambda request: handle(request=request, response=None))
page.on("response", lambda response: handle(response=response, request=None))
然后可以写一个handle自定义函数，args为response和request，然后后面想怎么处理数据都可以
"""
# setup logging
logging.basicConfig(format='%(asctime)s | %(levelname)s : %(message)s', level=logging.INFO)


def handle_json(json):
    # process our json data
    # print(json)
    for i in range(20):
        data_list = json['list'][i]
        # print(data_list)
        id = data_list['id']
        prodName = data_list['prodName']
        prodCat = data_list['prodCat']
        place = data_list['place']
        print(id, prodName, prodCat, place)


def handle(request, response):
    if response is not None:
        # response url 是网站请求数据的url
        if response.url == 'http://www.xinfadi.com.cn/getPriceData.html':
            handle_json(response.json())


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(ignore_https_errors=True)

    # Open new page
    page = context.new_page()

    page.on("request", lambda request: handle(request=request, response=None))
    page.on("response", lambda response: handle(response=response, request=None))
    # url是网页加载的URL
    url = 'http://www.xinfadi.com.cn/index.html'
    page.goto(url)
    # 然后之前看到有说道网站动态加载，拖动的问题。playwright可以直接用page.mouse.wheel(0, 300)解决
    page.wait_for_timeout(50000)
    # ---------------------
    context.close()
    page.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)