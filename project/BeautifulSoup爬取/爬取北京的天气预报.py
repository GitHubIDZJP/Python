import requests
from bs4 import BeautifulSoup
myHeaders = {
    'User-Agent':'Chrome/108.0.0.0'
}
url = 'https://www.tianqi.com/beijing/'
response = requests.get(url,headers=myHeaders)
# html = response.content.decode('utf-8')
# print(html)
soup = BeautifulSoup(response.text, 'lxml')
# temp = soup.findAll('ul', attrs={'class': 'raweather760'})
temp = soup.findAll('ul', class_='raweather760')
# weather = soup.find('div', attrs={'class': 'wea'}).get_text()
# print(temp)
for msg in temp:
    # a = msg.find('a',class_='d15').text.strip()
    # print(a)
    # city = msg.find('h5',class_=False).text.strip()
    city = msg.findAll('h5', attrs={'class':False})
    # print(city)
    print('城市数量:\n', len(city))
    for city_index  in city:
        print("城市:\n",city_index.text)

    # 会打印a里面的所有HTML元素值
    # a_weather_forecast_All_Msg = msg.find('a', attrs={'class':False}).text.strip()
    # a_weather_forecast = msg.a.attrs['title'].strip() #find('a', class_=False).string
    # print(a_weather_forecast)
    # a_href = msg.
    weather = msg.findAll('a', attrs={'class':False})
    # print(weather)
    print('天气数量:\n',len(weather))
    for weather_index in weather:
        print("天气预报:\n",weather_index.attrs['title'])

    a_href = msg.findAll('a', attrs={'class':False})
    print('天气预报链接数量\n',len(a_href))
    for a_href_index in a_href:
        print("天气预报链接:\n",a_href_index.attrs['href'])
# print('当前温度：', temp)
# print('天气状况：', weather)

#总共28个li
