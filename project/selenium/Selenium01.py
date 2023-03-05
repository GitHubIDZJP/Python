# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
#
# browser = webdriver.Chrome(ChromeDriverManager().install())
#
# browser.get('http://www.baidu.com')
# search = browser.find_element_by_id('kw')
# search.send_keys('python')
# search.send_keys(Keys.ENTER)
#
# # 关闭浏览器
# browser.close()

from selenium import webdriver  # 导入webdriver

driver = webdriver.Chrome()  # 实例化Chrome浏览器
driver.get("http://www.baidu.com")  # 打开http://www.baidu.com

