import csv
import pprint
import requests

url = 'https://movie.douban.com/j/chart/top_list'
start = input('从库中第几部电影取：')
limit = input('取几部：')
param = {
    'type': '24',
    'interval_id': '100:90',
    'action': '',
    'start': start,
    'limit': limit}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62'}
response = requests.get(url=url, params=param, headers=headers)
list_data = response.json()
pprint.pprint(list_data)

# 拿到的的确是两条数据，
# 然后从其中选择自己想要的数据出来，进行可视化处理，保存为csv格式
f = open('./豆瓣电影数据.csv', 'w', encoding='utf-8-sig', newline='')  # a 是追加保存
csv_write = csv.DictWriter(f, fieldnames=[
    '电影名',
    '主演人数',
    '主演',
    '评分',
    '上映时间',
    '类型',
    '评论数',
    '拍摄国家',
])
csv_write.writeheader()

for i in list_data:
    dic = {
        '电影名': i['title'],
        '主演人数': i['actor_count'],
        '主演': i['actors'],
        '评分': i['score'],
        '上映时间': i['release_date'],
        '类型': i['types'],
        '评论数': i['vote_count'],
        '拍摄国家': i['regions']
    }
    print(dic)
    csv_write.writerow(dic)

