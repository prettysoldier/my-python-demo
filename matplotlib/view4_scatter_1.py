
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %matplotlib inline
np.random.seed(2000)
y = np.random.standard_normal((1000, 2))

plt.plot(y[:, 0], y[:, 1], 'ro')
plt.grid()
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter')

plt.show()
