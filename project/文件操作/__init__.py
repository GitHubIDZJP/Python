import json

import xlrd
#读取xssl文件

wb = xlrd.text('爬虫兼职.xlsl')
sh = wb.sheet_by_name()


#读取json文件
# path = r'./爬虫案例/爬虫兼职.xlsl'
#
# with open(path,"r") as file:
#     a = open(path)
#     rowData = json.load(a)
# for printData in rowData:
#     print(printData)
