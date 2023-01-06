

import pandas as pd

date={'code':[20,20,19,19,20],'type':['hive','hive','clickhouse','clickhouse','hive'],'datetime':['2022-5-23','2022-5-23','2022-5-23','2022-5-23','2022-5-24']}

df=pd.DataFrame(date)

time_data = pd.to_datetime(df["datetime"],format='%Y-%m-%d')

df['datetime']=time_data

# df.dtypes
print(df.dtypes)
# df.to_json(orient='records')
'''

code                 int64
type                object
datetime    datetime64[ns]
dtype: object'''

df.to_json('/Users/zoujunping/Python/代码run后保存路径/json.json',orient='values')