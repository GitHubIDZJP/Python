import requests
url = 'http://yjs.cqupt.edu.cn/list.jsp?urltype=tree.TreeTempUrl&wbtreeid=1180'
# url = 'https://baidu.com'
myHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'Cookie':'mLvnBZTNP4mtS=5.MxaNXarcbffs9Sm0iXTQHbG9yl9_c2qfX4ofLiqSurCNVVGICnjh.RIvLHTP6qYSN4dTPgGb66Q_8hjuxULfq; JSESSIONID=4C9E28A09285ADE60C269B9720739ABC; mLvnBZTNP4mtT=BR9670wna82lkyzeXbTdQYu1lBL2I7BQlK2wSrzjggse7hzLvhxLvqAro4RJu54PSw3GP_F8pv3ioMUZziqp2zQfc4jW21qh9ek28L5.1UpG65dHlEB3QbwBxgyGGuNs1JEXPqF1zbehtMtOt.4M_tYfPIU7qx1nBXPQJohrtiXdUOKDRYkLEqIKYOKpwpWsREUJWIZ7v1qCx62Nl7CTTsRVSiDY.KdOi4sFYoPP3wVhS.EW9kQa9.yB2R1.VFSd1j9Co1iRz5YHfy9MyHgybBahsM0L7pmmCxzqshxS2MohAdJKwged2asGY04x.RaN03aj.baudnIvZ3xOIVEn3kJ0q57RpB6RKkVVcXP2PnELujEx7BNqyo8lHzCNUeET'
}
result=requests.get(url,headers=myHeaders)

# print(result.content.decode('utf-8'))
print(result.text)
print('----------------------------')
# print('sdsd')
# with open(r'/Users/zoujunping/python采集资源/豆瓣排行榜/index.html','wb') as f:
#     f.write(result.content)
#     print('保存成功 ! ! !')