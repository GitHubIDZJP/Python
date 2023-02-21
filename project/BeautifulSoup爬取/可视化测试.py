import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import leastsq
matplotlib.get_cachedir()
font = {
    "family": "Microsoft YaHei"
}
matplotlib.rc("font", **font)
plt.figure(figsize=(9, 9))
X = np.array([8.19, 2.72, 6.39, 8.71, 4.7, 2.66, 3.78])
Y = np.array([7.01, 2.78, 6.47, 6.71, 4.1, 4.23, 4.05])


# 计算以p为参数的直线与原始数据之间误差
def f(p):
    k, b = p
    return (Y - (k * X + b))


# leastsq使得f的输出数组的平方和最小，参数初始值为[1,0]
r = leastsq(f, [1, 0])
k, b = r[0]
plt.scatter(X, Y, s=100, alpha=1.0, marker='o', label=u'数据点')
x = np.linspace(0, 10, 1000)
y = k * x + b
ax = plt.gca()
plt.plot(x, y, color='r', linewidth=5, linestyle=":", markersize=20, label=u'拟合曲线')
plt.legend(loc=0, numpoints=1)
leg = plt.gca().get_legend()
ltext = leg.get_texts()
plt.setp(ltext, fontsize='xx-large')
plt.xlabel(u'安培/A')
plt.ylabel(u'伏特/V')
plt.xlim(0, x.max() * 1.1)
plt.ylim(0, y.max() * 1.1)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(loc='upper left')
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.show()
