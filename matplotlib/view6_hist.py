
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %matplotlib inline
np.random.seed(2000)
y = np.random.standard_normal((1000, 2))

plt.hist(y, label=['1st', '2nd'], bins=25)
plt.legend()
plt.grid()
plt.xlabel('value')
plt.ylabel('frequency')
plt.title('Histogram')

plt.show()
