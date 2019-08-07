
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon


# 定义函数
def func(x):
    return 0.5 * np.exp(x) + 1


# 定义积分区间
x = np.linspace(0, 2)
y = func(x)
# 绘制函数图形
fig, ax = plt.subplots()
plt.plot(x, y, 'b', lw=2)
plt.ylim(ymin=0)
# 生成阴影部分
a, b = 0.5, 1.5
Ix = np.linspace(a, b)
Iy = func(Ix)
verts = [(a, 0)] + list(zip(Ix, Iy)) + [(b, 0)]
poly = Polygon(verts, facecolor='07', edgecolor='0.5')
ax.add_patch(poly)
# 用plt.text和plt.figtext在图形上添加公式和坐标轴标签
plt.text(0.5 * (a + b), 1, r"$\int_a^b f(x)\mathrm{d}x$", horizontalalignment='center', fontsize=20)
plt.figtext(0.9, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')
# 设置刻度标签
ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([func(a), func(b)])
ax.set_yticklabels(('$f(a)$', '$(b)$'))

plt.grid()
plt.show()

