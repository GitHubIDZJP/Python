from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://ggzyjy.baiyin.gov.cn/InfoPage/TradeInfomation.aspx?state=3'
browser = webdriver.Chrome()
browser.get(url)

li_list = browser.find_elements(By.XPATH, '//ul[@id="tradMainWrap"]/li')
for li in li_list:
    url_detail = li.find_element(By.XPATH, './a').get_attribute('href')
    print(url_detail)