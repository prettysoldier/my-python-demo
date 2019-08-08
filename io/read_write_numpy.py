import numpy as np

dtime = np.arange('2014-01-01', '2015-01-01', dtype='datetime64[M]')
# print(dtime)

path = '/test/python/'
np.save(path + 'array', dtime)

read_data = np.load(path + 'array')
print(read_data)
