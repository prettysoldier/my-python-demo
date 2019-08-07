# 结构数组
import numpy as np

a = np.array([1, 2])
print(type(a))

dt = np.dtype([('name', 'S20'), ('age', 'i4'), ('test', 'i4', 2)])
s = np.array([('zhangsan', 30, (0, 1)),
              ('lisi', 32, (2, 3))], dtype=dt)

print(s)
print(type(s))
print(s['name'])
print('平均年龄：%s' %s['age'].mean())
