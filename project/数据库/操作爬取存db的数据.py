

import pymysql
# 1
conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    database='pdb',
    charset='utf8',
    autocommit=True
)
#2 光标
cursor = conn.cursor(pymysql.cursors.DictCursor)#生成游标对象

#表1: python_table
#表2：push_db
sql = 'select * from push_db'

cursor.execute(sql)  # 执行(execute)传入的sql语句


# print(cursor.fetchone())  # 只获取一条数据
# cursor.scroll(2,'absolute')  # 绝对定位，控制光标移动   absolute相对于其实位置 往后移动几位
# cursor.scroll(1,'relative')  # 相对定位，relative相对于当前位置 往后移动几位
print(cursor.fetchall()) # 获取所有的数据  返回的结果是一个列表,，可以for循环再依次取

# 5
cursor.close()
# 6
conn.close()




