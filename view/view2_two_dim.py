
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 散点图
np.random.seed(2000)
y = np.random.standard_normal((20, 2)).cumsum(axis=0)

y[:, 0] = y[:, 0] * 100
print(y)
fig, ax1 = plt.subplots()
# 左轴
plt.plot(y[:, 0], 'r', lw=2, label='1st')
plt.plot(y[:, 0], 'ko')
plt.grid()
plt.xlabel('index')
plt.ylabel('value 1st')
plt.legend()
# 右轴
ax2 = ax1.twinx()
plt.plot(y[:, 1], 'b', label='2st', )
plt.plot(y[:, 1], 'ko')
plt.legend(loc=0)
plt.ylabel('value 2st')

plt.show()
