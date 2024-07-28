# 直方图
# matplotlib.pyplot.hist(x, bins=None, range=None, density=False, weights=None, cumulative=False, bottom=None,
# histtype='bar', align='mid',orientation='vertical', rwidth=None, log=False, color=None, label=None, stacked=False, **kwargs)
# x：表示要绘制直方图的数据，可以是一个一维数组或列表。
# bins：可选参数，表示直方图的箱数(分成几组)。默认为10。 重要参数
# range：可选参数，表示直方图的值域范围，可以是一个二元组或列表。默认为None，即使用数据中的最小值和最大值。
# density：可选参数，表示是否将直方图归一化。默认为False，即直方图的高度为每个箱子内的样本数，而不是频率或概率密度。
# weights：可选参数，表示每个数据点的权重。默认为None。
# cumulative：可选参数，表示是否绘制累积分布图。默认为False。 后一个为前一个+当前值
# bottom：可选参数，表示直方图的起始高度。默认为None。
# histtype：可选参数，表示直方图的类型，可以是'bar'、'barstacked'、'step'、'stepfilled'等。默认为'bar'。
# align：可选参数，表示直方图箱子的对齐方式，可以是'left'、'mid'、'right'。默认为'mid'。
# orientation：可选参数，表示直方图的方向，可以是'vertical'、'horizontal'。默认为'vertical'。
# rwidth：可选参数，表示每个箱子的宽度。默认为None。
# log：可选参数，表示是否在y轴上使用对数刻度。默认为False。
# color：可选参数，表示直方图的颜色。
# label：可选参数，表示直方图的标签。
# stacked：可选参数，表示是否堆叠不同的直方图。默认为False。
# **kwargs：可选参数，表示其他绘图参数。
import matplotlib.pyplot as plt
import numpy as np

# 生成一组随机数据
fig = plt.figure()
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
data = np.random.randn(1000)

# 绘制直方图
ax.hist(data, bins=20, color='skyblue', alpha=0.8)  # bins除了写个数，还能自己写范围，用列表表示
ax.hist(data, bins=[-4, -3, -2, -1, 0, 1, 2, 3, 4], color='skyblue', alpha=0.8, density=True)  # bins除了写个数，还能自己写范围，用列表表示
ax.set_title('Histogram of data')

# 设置图表属性
ax.set_xlabel('Value')
ax.set_ylabel('Frequency')

# 显示图表
plt.show()