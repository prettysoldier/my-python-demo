
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %matplotlib inline
np.random.seed(2000)
y = np.random.standard_normal((1000, 2))
print(len(y))
c = np.random.randint(0, 10, len(y))
plt.scatter(y[:, 0], y[:, 1], c=c, marker='o')
plt.colorbar()
plt.grid()
plt.xlabel('1st')
plt.ylabel('2nd')
plt.title('Scatter')


plt.show()
