
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# %matplotlib inline
np.random.seed(2000)
y = np.random.standard_normal((100, 2))

fig, ax = plt.subplots()
plt.boxplot(y)
plt.grid()
plt.setp(ax, xticklabels=['1st', '2nd'])
plt.xlabel('data set')
plt.ylabel('value')
plt.title('Boxplot')

plt.show()
