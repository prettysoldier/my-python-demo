import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 1, 0.01)   # 这里就没额外考虑log的值域了，会有个warning
print(x)
entropy = -1 * (x * np.log(x) + (1 - x) * np.log(1 - x))  # ∑ p(x)logp(x)

plt.plot(x, entropy)
plt.xlabel('p'), plt.ylabel('entropy')
plt.grid(), plt.show()
