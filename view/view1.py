
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %matplotlib inline
np.random.seed(1000)
y = np.random.standard_normal(20)

x = range(len(y))

plt.grid(True)
plt.axis('tight')
plt.xlim(-1, 20)
plt.ylim(np.min(y.cumsum()) - 1, np.max(y.cumsum()) + 1)
# plt.figure(figsize=(7, 4))
line = plt.plot(x, y.cumsum(), 'b-')
# plt.setp(line, linestyle='--')
plt.plot(x, y.cumsum(), 'r1')
plt.xlabel('index')
plt.ylabel('value')
plt.title('sample example')
plt.show()
