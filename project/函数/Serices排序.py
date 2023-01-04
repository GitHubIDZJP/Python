import pandas as pd


'''
排序:
默认 ascending=True 升序 ：从首位到末尾开始排
'''
df = pd.Series([1, 2, 3, 4], index=["A", "B", "C", "D"])
print(df.sort_index())
'''
打印: 升序--->
A    1
B    2
C    3
D    4
'''
# 降序：从末尾到首位开始排
print(df.sort_index(ascending=False))
'''
D    4
C    3
B    2
A    1
'''





