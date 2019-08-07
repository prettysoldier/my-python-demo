import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import time

DAX = pdr.DataReader(name='^GDAXI', data_source='yahoo', start='2012-1-1')
# print(DAX.tail())
# print(DAX.info())
# DAX['Close'].plot()

# start = time.time_ns()
# DAX['Ret_Loop'] = 0.0
# for i in range(1, len(DAX)):
#     DAX['Ret_Loop'][i] = np.log(DAX['Close'][i] / DAX['Close'][i - 1])
# print('耗时：%sms' % ((time.time_ns() - start) / 1000_000))
# print(DAX[['Close', 'Ret_Loop']].tail())
# print('--------------')

start2 = time.time_ns()
DAX['Return'] = np.log(DAX['Close'] / DAX['Close'].shift(1))
# print('耗时：%sms' % ((time.time_ns() - start2) / 1000_000))
# print(DAX[['Close', 'Return']].tail())

# DAX[['Close', 'Return']].plot(subplots=True, style='b')
DAX['42d'] = DAX['Close'].rolling(42).mean()
DAX['252d'] = DAX['Close'].rolling(252).mean()
DAX[['Close', '42d', '252d']].plot()

plt.show()





