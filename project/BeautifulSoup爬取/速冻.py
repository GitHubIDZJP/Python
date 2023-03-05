import requests
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# url = 'https://news.ifeng.com/c/special/7uLj4F83Cqm'
# ua = UserAgent(verify_ssl=False)
myHeaders = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    # 'User-Agent':ua.random,
    'Cookie':'userid=1677592548071_s777p95837'
}


# 发送HTTP请求获取网页内容
url = 'https://news.ifeng.com/c/special/7uLj4F83Cqm'
response = requests.get(url)

# 使用BeautifulSoup解析HTML页面
soup = BeautifulSoup(response.text, 'html.parser')

# 获取累计确诊和现存确诊的标签
total_confirm_tag = soup.find('div', class_='index_tr_list_4IrYQ')
print(total_confirm_tag)
# current_confirm_tag = soup.find('div', {'class': 'p_line'}).find_all('span')[2]
#
# # 提取标签中的文本内容
# total_confirm = total_confirm_tag.text
# current_confirm = current_confirm_tag.text
#
# # 输出结果
# print('累计确诊：', total_confirm)
# print('现存确诊：', current_confirm)
