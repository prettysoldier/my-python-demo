import numpy as np
import pickle as pk
import pandas as pd

path = '/test/python/'
rows = 5000
a = np.random.standard_normal((rows, 5))
t = pd.date_range(start='2014/1/1', periods=rows, freq='H')
print(t)
csv_file = open(path + 'data.csv', 'w')
header = 'date,no1,no2,no3,no4,no5\n'
csv_file.write(header)

for _t, (no1, no2, no3, no4, no5) in zip(t, a):
    s = '%s,%f,%f,%f,%f,%f\n' % (_t, no1, no2, no3, no4, no5)
    csv_file.write(s)
csv_file.close()

csv_file_read = open(path + 'data.csv', 'r')
for i in range(5):
    print(csv_file_read.readline())

