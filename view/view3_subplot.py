
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %matplotlib inline
np.random.seed(2000)
y = np.random.standard_normal((20, 2)).cumsum(axis=0)
y[:, 0] = y[:, 0] * 100
print(y)
# 左图
plt.subplot(211)
plt.plot(y[:, 0], 'r', lw=2, label='1st')
plt.plot(y[:, 0], 'ko')
plt.grid()
plt.xlabel('index')
plt.ylabel('value 1st')
plt.legend()
# 右图
plt.subplot(212)
plt.bar(np.arange(len(y)), y[:, 1], width=0.5, label='2st')
plt.grid()
plt.xlabel('index')
plt.ylabel('value 2st')
plt.legend()

plt.show()
