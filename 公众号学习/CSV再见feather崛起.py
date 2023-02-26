# https://mp.weixin.qq.com/s/pz7MZTKc8ZmxIh9C9IFG3w
'''
pip install feather -format

# Anaconda
conda install -c conda-forgefeather-format


'''
import feather
import numpy as np
import pandas as pd
# 通过一个较大的数据集举例，需要 Feather、Numpy 和 pandas 来一起配合。数据集有 5 列和 1000 万行随机数
np.random.seed = 42
df_size = 10000000

df = pd.DataFrame({
    'a': np.random.rand(df_size),
    'b': np.random.rand(df_size),
    'c': np.random.rand(df_size),
    'd': np.random.rand(df_size),
    'e': np.random.rand(df_size)
})
df.head()
print(df)

'''
差距巨大，有木有！原生 Feather(图中的Native Feather)比 CSV 快了将近 150 倍左右。如果使用 pandas 处理 Feather 文件并没有太大关系，但与 CSV 相比，速度的提高是非常显著的。

'''

