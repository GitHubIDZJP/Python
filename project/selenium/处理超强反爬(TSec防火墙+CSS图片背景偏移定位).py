from selenium.webdriver import ChromeOptions
from selenium import webdriver
browser = webdriver.Chrome()

option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
option.add_experimental_option('useAutomationExtension', False)
option.add_argument(
    'user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36')
option.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=option)

with open('stealth.min.js') as f:
    js = f.read()
browser.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
    'source': js
})
url = 'http://hotels.huazhu.com/inthotel/detail/9005308'
browser.get(url)


'''
会闪退

'''