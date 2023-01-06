
#读取xssl文件
'''
xlrd库：读取excel文件，支持xls和xlsx格式（最新版好像不支持xlsx，解决方法可自行搜索）。
如果强制读取，则会报错:
line 60, in inspect_format with open(path, "rb") as f:
xlwt库：写入excel文件，只支持xls格式。
所有读取文件后缀.xlsx会报错
'''
import xlrd #已经被pandas放弃

file_path = '/Users/zoujunping/Python/代码run后保存路径/爬虫兼职.xls'
data = xlrd.open_workbook(file_path)
table = data.sheet_by_name('Sheet0')

# 获取总行数
nrows = table.nrows
# 获取总列数
ncols = table.ncols

# 获取一行的全部数值，例如第5行
row_value = table.row_values(5)
# 获取一列的全部数值，例如第6列
col_values = table.col_values(6)

# 获取一个单元格的数值，例如第5行第6列
cell_value = table.cell(5, 6).value


