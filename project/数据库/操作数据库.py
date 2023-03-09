import pymysql

conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='pdb',
    charset='utf8',
    autocommit=True
)

cursor = conn.cursor(pymysql.cursors.DictCursor)  # 产生游标对象，将查询出来的结果制作成字典的形式返回
sql = 'select * from teacher'
cursor.execute(sql)  # 执行传入的sql语句
# print(cursor.fetchone())  # 只获取一条数据
# print(cursor.fetchone())  # 只获取一条数据
# print(cursor.fetchone())  # 只获取一条数据
# print(cursor.fetchone())  # 只获取一条数据
# cursor.scroll(2,'absolute')  # 绝对定位，控制光标移动   absolute相对于其实位置 往后移动几位
# cursor.scroll(1,'relative')  # 相对定位，relative相对于当前位置 往后移动几位
print(cursor.fetchall())  # 获取所有的数据  返回的结果是一个列表
cursor.close()
conn.close()

'''
终端输入() 说明操作成功
1 mysql -uroot -p
2 密码: 123456

'''