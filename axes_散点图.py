# matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None,
# alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)
# x，y：长度相同的数组，也就是我们即将绘制散点图的数据点，输入数据。  注意要长度相等
#
# s：点的大小，默认 20，也可以是个数组，数组每个参数为对应点的大小。
#
# c：点的颜色，默认蓝色 'b'，也可以是个 RGB 或 RGBA 二维行数组。
#
# marker：点的样式，默认小圆圈 'o'。
#
# cmap：Colormap，默认 None，标量或者是一个 colormap 的名字，只有 c 是一个浮点数数组的时才使用。如果没有申明就是 image.cmap。  afmhot_r,viridis
#
# norm：Normalize，默认 None，数据亮度在 0-1 之间，只有 c 是一个浮点数的数组的时才使用。
#
# vmin，vmax：：亮度设置，在 norm 参数存在时会忽略。
#
# alpha：：透明度设置，0-1 之间，默认 None，即不透明。
#
# linewidths：：标记点的长度。
#
# edgecolors：：颜色或颜色序列，默认为 'face'，可选值有 'face', 'none', None。
#
# plotnonfinite：：布尔值，设置是否使用非限定的 c ( inf, -inf 或 nan) 绘制点。
#
# **kwargs：：其他参数。
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])  # x轴序列
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])  # y轴序列
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])  # 颜色序列

sca = ax.scatter(x, y, c=colors,cmap='afmhot_r')
plt.colorbar(sca)  # 将颜色条放在图片旁边
plt.show()
