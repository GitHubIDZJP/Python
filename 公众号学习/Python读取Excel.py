# 02 文件内容
# #与read_csv一样，需要注意，Mac和Windows中的路径写法不一样。
# io为第一个参数，没有默认值，也不能为空，根据Python的语法，第一个参数传参时可以不写。可以传入本地文件名或者远程文件的URL：
# # 字符串、字节、Excel文件、xlrd.Book实例、路径对象或者类似文件的对象
# # 本地相对路径
# pd.read_excel('data/data.xlsx') # 注意目录层级
# pd.read_excel('data.xls') # 如果文件与代码文件在同一目录下
# # 本地绝对路径
# pd.read_excel('/user/gairuo/data/data.xlsx')
# # 使用URL
# pd.read_excel('https://www.gairuo.com/file/data/dataset/team.xlsx')
#
#
# 03 表格
#
# sheet_name可以指定Excel文件读取哪个sheet，如果不指定，默认读取第一个。
#
# # 字符串、整型、列表、None，默认为0
# pd.read_excel('tmp.xlsx', sheet_name=1) # 第二个sheet
# pd.read_excel('tmp.xlsx', sheet_name='总结表') # 按sheet的名字
#
# # 读取第一个、第二个、名为Sheet5的sheet，返回一个df组成的字典
# dfs = pd.read_excel('tmp.xlsx', sheet_name=[0, 1, "Sheet5"])
# dfs = pd.read_excel('tmp.xlsx', sheet_name=None) # 所有sheet
# dfs['Sheet5'] # 读取时按sheet名
#
#
# 04 表头
#
# 数据的表头参数为header，如不指定，默认为第一行。
#
# # 整型、整型组成的列表，默认为 0
# pd.read_excel('tmp.xlsx', header=None)  # 不设表头
# pd.read_excel('tmp.xlsx', header=2)  # 第三行为表头
# pd.read_excel('tmp.xlsx', header=[0, 1])  # 两层表头，多层索引
#
#
# 05 列名
#
# 用names指定列名，也就是表头的名称，如不指定，默认为表头的名称。
#
# # 序列，默认为None
# pd.read_excel('tmp.xlsx', names=['姓名', '年龄', '成绩'])
# pd.read_excel('tmp.xlsx', names=c_list) # 传入列表变量
# # 没有表头，需要设置为None
# pd.read_excel('tmp.xlsx', header=None, names=None)
#
#
