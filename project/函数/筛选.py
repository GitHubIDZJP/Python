
import pandas as pd
import numpy as np
'''
1 np.random.randn:返回一个或多个样本值(随机值)
'''
df = pd.DataFrame(np.random.randn(3, 3), columns=['A', 'B', 'C'])
print(df)
'''
          A         B         C
0 -0.287300 -2.457867  0.157718
1 -1.389967 -0.789644  0.176444
2 -0.616758  0.282540 -0.563630
'''
# 布尔索引判断：A列大于1的数
print(df['A'] > 1)
'''
0    False
1    False
2    False
'''
# 布尔索引筛选：A列中大于1的行
print(df[df['A'] > 1])

''''

'''

# 2between()：赛选指定区间的行
b_data = {'name': ['小红', '小明', '小白', '小黑'], 'age': [10, 20, 30, 25]}
b_df = pd.DataFrame(b_data)
print(b_df)
''' 
    naem  age
0   小红   10
1   小明   20
2   小白   30
3   小黑   25
'''
# 判断年龄是否在20-30之间
print(b_df['age'].between(20, 30))
'''
0    False 10<20 所以位false
1     True  20 在20-30之间 为true
2     True 30 在20-30之间 为true
3     True 25 在20-30之间 为true
'''
# 筛选年龄在20-30之间的行
print(b_df[b_df['age'].between(20, 30)])
'''
    name  age
1   小明   20
2   小白   30
3   小黑   25
'''

#3 isin()
#isin0接收一个列表，可以同时判断数据是否与多个值相等，若与其中的某个值相等则返回 True，否则则为 False


isin_data = [['foo', 'one', 'small', 1], ['foo', 'one', 'large', 5],
['bar', 'one', 'small', 10], ['bar', 'two', 'samll', 10],
['bar', 'two', 'large', 50]]
isin_df = pd.DataFrame(isin_data, columns=['A', 'B', 'C', 'D'])
print(isin_df)
''''
3位数组里没有一个数娱 a  b c d 相等的
    A    B      C   D
0  foo  one  small   1
1  foo  one  large   5
2  bar  one  small  10
3  bar  two  samll  10
4  bar  two  large  50
'''

#3.1 单例筛选
# df[df[列名]isin([异常值])]
# 1. 接收一个值：判断A列中的值是否为foo
i_d_v = isin_df['A'].isin(['foo'])
print(i_d_v)
'''
A列中前2位是位foo，true
0     True
1     True
2    False
3    False
4    False
'''

#3.2 多列筛选(multicolumn_filtering)
# 同时满足用&连接，或的话用|连接
multicolumn_filtering = isin_df[isin_df['A'].isin(['bar']) & isin_df['B'].isin(['one'])]
print(multicolumn_filtering )

'''
     A    B      C   D
2  bar  one  small  10
'''

#3.3: 通过字典的形式传递多个条件
# {'某列：[条件];某列：[条件]}
# 这种方法不符合的位置都会显示NAN
print(isin_df[isin_df.isin({'A':['bar'],'C':['small']})])

'''     A    B      C   D
0  NaN  NaN  small NaN
1  NaN  NaN    NaN NaN
2  bar  NaN  small NaN
3  bar  NaN    NaN NaN
4  bar  NaN    NaN NaN
'''

#3.4 删除行的异常值
# 因为isin()返还的是boolean的DataFrame，在里面的是True，不在里面的是False，所以我们只需要对它进行异或取反即可。

#删除A列种的foo行
print(isin_df[True^isin_df['A'].isin(['foo'])])
# 还有个新写法
# isin_df[True^isin_df['A']=='foo']

'''
本来A里有foo和bar的，现在只剩下Bar了
     A    B      C   D
2  bar  one  small  10
3  bar  two  samll  10
4  bar  two  large  50
'''

#4.提取数据： loc和iloc
'''
loc()函数和iloc()函数的区别在于：
   loc(函数是通过索引名称提取数据
    iloc()函数通过行和列的下标提取数据
'''

tq_data = [['foo', 'one', 'small', 1], ['foo', 'one', 'large', 5],['bar', 'one', 'small', 10], ['bar', 'two', 'samll', 10],['bar', 'two', 'large', 50]]
tq_df = pd.DataFrame(tq_data, columns=['A', 'B', 'C', 'D'], index=['a', 'b', 'c', 'd', 'e'])
print(tq_df)
'''
打印全部数据
     A    B      C   D
a  foo  one  small   1
b  foo  one  large   5
c  bar  one  small  10
d  bar  two  samll  10
e  bar  two  large  50
'''

#开始做数据提取--通过名称

#提取行数据loc
print(tq_df.loc['a'])

'''
提取a对应行的数据loc
A      foo
B      one
C    small
D        1
'''
#提取行a的数据iloc--通过索引
print(tq_df.iloc[0])
'''
A      foo
B      one
C    small
D        1
'''
#提取列数据loc
print(tq_df.loc[:,['A']])
#提取多列数据  tq_df.loc[:,['A','B','C']]
#提取指定行，列数据
# loc取索引为a、d，并且列名也为A、D的行和列
# tq_df.loc[['a','d'],['A','D']]
#提取所有数据
# tq_df.loc[:,:]
'''
     A
a  foo
b  foo
c  bar
d  bar
e  bar
'''
#提取行a的数据iloc
print(tq_df.iloc[:,[0]])
#提取多列数据  print(tq_df.iloc[:,[0:3]])
#loc取索引为a、d，并且列名也为A、D的行和列
# tq_df.iloc[[0,3],[0,3]]
#提取所有数据
# tq_df.iloc[:,:]
'''
     A
a  foo
b  foo
c  bar
d  bar
e  bar
'''

# 提取指定数据行

#loc提取A列只为foo的行
# tq_df[df['A'] == 'foo']
'''
     A    B      C  D
a  foo  one  small  1
b  foo  one  large  5
'''

#loc提取D值大于等于10的行
# tq_df[tq_df['D'] >= 10]
'''
     A    B      C   D
c  bar  one  small  10
d  bar  two  samll  10
e  bar  two  large  50
'''