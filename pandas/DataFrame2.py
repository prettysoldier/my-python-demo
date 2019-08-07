import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

a = np.random.standard_normal((9, 4))
a = a.round(6)
# print(a)

df = pd.DataFrame(a)
df.columns = ['N1', 'N2', 'N3', 'N4']
# print(df)
# print(df['N3'][3])

dates = pd.date_range('2015-1-1', periods=9, freq='M')
# print(dates)

df.index = dates
# print(df)

arr = np.array(df)
# print(arr)

# print(df.sum())
# print(df.mean())
# print(df.cumsum)
# print(df.describe())
# print(np.abs(df))

# df.cumsum().plot()
# plt.show()

# print(type(df))
# print(type(df['N1']))

# df['N1'].cumsum().plot()
# plt.show()

df['Quarter'] = ['Q1', 'Q1', 'Q1', 'Q2', 'Q2', 'Q2', 'Q3', 'Q3', 'Q3']
# print(df)
groups = df.groupby('Quarter')
# print(groups)
# print(type(groups))
# print(groups.max())
# print(type(groups.mean()))
# print(groups.describe())

df['Odd_Even'] = ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even', 'Odd']
groups2 = df.groupby(['Quarter', 'Odd_Even'])
# print(groups2.size())
print(groups2.mean())