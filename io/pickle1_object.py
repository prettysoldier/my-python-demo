import numpy as np
import random
import pickle as pk
"""
序列化读写磁盘
"""
path = '/test/python/'
a = [random.gauss(1.5, 2) for i in range(100_0000)]

# pkl_file_write = open(path + 'data.pkl', 'wb')
# pk.dump(a, pkl_file_write)
# print(pkl_file_write)

# pkl_file_read = open(path + 'data.pkl', 'rb')
# b = pk.load(pkl_file_read)
# print(b[:5])

# print(np.allclose(np.array(a), np.array(b)))
# print(np.sum(np.array(a) - np.array(b)))

# 存储ndarray比list更快，文件很小
# pkl_file_write2 = open(path + 'data2.pkl', 'wb')
# pk.dump(np.array(a), pkl_file_write2)
# pk.dump(np.array(a) ** 2, pkl_file_write2)
# pkl_file_write2.close()
#
# FIFO原则保存和读取对象
# pkl_file_read2 = open(path + 'data2.pkl', 'rb')
# print(pk.load(pkl_file_read2))
# print(pk.load(pkl_file_read2))


pkl_file_write3 = open(path + 'data3.pkl', 'wb')
pk.dump({'x': np.array(a), 'y': np.array(a) ** 2}, pkl_file_write3)
pkl_file_write3.close()

pkl_file_read3 = open(path + 'data3.pkl', 'rb')
data = pk.load(pkl_file_read3)
pkl_file_read3.close()
for key in data.keys():
    print(key, data[key][:4])
