import numpy as np
import pandas as pd

df = pd.DataFrame([10, 20, 30, 40], columns=['numbers'], index=['a', 'b', 'c', 'd'])

df2 = pd.DataFrame([1, 4, 6, 8], columns=['new'], index=['a', 'b', 'c', 'y'])
df_join = df.join(df2)
print(df)
print(df2)
# append join 等方法只会复制原来的dataframe, 而不会修改原来的dataframe
print(df_join)

