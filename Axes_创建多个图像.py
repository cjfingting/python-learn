# subplot(nrows,ncols,index) 返回指定网格位置的axes对象  可随意切分，用数字代表
# 以上函数将整个绘图区域分成 nrows 行和 ncols 列，
# 然后从左到右，从上到下的顺序对每个子区域进行编号 1...N ，左上的子区域的编号为 1、右下的区域编号为 N，编号可以通过参数 index 来设置
# 如果三个参数都小于10，则可以省略逗号，连续写出
# import matplotlib.pyplot as plt
# import numpy as np
#
# fig = plt.figure(figsize=(12, 6))
# #plot 1:
# xpoints = np.array([0, 6])
# ypoints = np.array([0, 100])
#
# ax1 = plt.subplot(2, 1, 1)
# ax1.plot(xpoints,ypoints)
# ax1.set_title("plot 1")
#
# #plot 2:
# x = np.array([1, 2, 3, 4])
# y = np.array([1, 4, 9, 16])
#
# ax2 = plt.subplot(2, 1, 2)
# ax2.plot(x,y)
# ax2.set_title("plot 2")
#
# plt.suptitle("RUNOOB subplot Test")  # 主标题
# plt.show()
import math

# matplotlib.pyplot.subplots(nrows=1, ncols=1, *, sharex=False, sharey=False, squeeze=True, subplot_kw=None, gridspec_kw=None, **fig_kw)
# 可以将多图分给一个axs对象，用下标表示每一个,也可以将多个图分给多个axs对象
# nrows：默认为 1，设置图表的行数。
# ncols：默认为 1，设置图表的列数。
# sharex、sharey：设置 x、y 轴是否共享属性，默认为 false，可设置为 'none'、'all'、'row' 或 'col'。
# False 或 none 每个子图的 x 轴或 y 轴都是独立的，True 或 'all'：所有子图共享 x 轴或 y 轴，
# 'row' 设置每个子图行共享一个 x 轴或 y 轴，'col'：设置每个子图列共享一个 x 轴或 y 轴。
# squeeze：布尔值，默认为 True，表示额外的维度从返回的 Axes(轴)对象中挤出，对于 N*1 或 1*N 个子图，返回一个 1 维数组，
# 对于 N*M，N>1 和 M>1，返回一个 2 维数组。如果设置为 False，则不进行挤压操作，返回一个元素为 Axes 实例的2维数组，即使它最终是1x1。
# subplot_kw：可选，字典类型。把字典的关键字传递给 add_subplot() 来创建每个子图。
# gridspec_kw：可选，字典类型。把字典的关键字传递给 GridSpec 构造函数创建子图放在网格里(grid)。
# **fig_kw：把详细的关键字参数传给 figure() 函数。
# import matplotlib.pyplot as plt
# import numpy as np
#
# 创建一些测试数据 -- 图1
# x = np.linspace(0, 2*np.pi, 400)
# y = np.sin(x**2)

# 创建一个画像和子图 -- 图2
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')

# 创建两个子图 -- 图3
# f, (ax1, ax2) = plt.subplots(1, 2, sharey=False)  # 共享y轴
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis')
# ax2.scatter(x, y)

# 创建四个子图 -- 图4
# 创建极坐标系
# fig, axs = plt.subplots(2,3,subplot_kw=dict(polar=True))
# axs[0, 0].plot(x, y)
# axs[1, 1].scatter(x, y)
# #
# # 共享 x 轴
# plt.subplots(2, 2, sharex='col')
#
# # 共享 y 轴
# plt.subplots(2, 2, sharey='row')
#
# # 共享 x 轴和 y 轴
# plt.subplots(2, 2, sharex='all', sharey='all')
#
# # 这个也是共享 x 轴和 y 轴
# plt.subplots(2, 2, sharex=True, sharey=True)
#
# # 创建标识为 10 的图，已经存在的则删除
# fig, ax = plt.subplots(num=10, clear=True)

# plt.show()

# subplot2grid(shape,loc,colspan,rowspan)
# shape 网格多少,元组(x,y)
# loc 起始位置,元组(x,y)
# colspan 占几列
# rowspan 占几行

# import matplotlib.pyplot as plt
# import numpy as np
# # fig = plt.subplot2grid((3,3)) 报错，不能分开写，得全部写在一起
# ax1 = plt.subplot2grid((3, 3), loc=(0, 0), colspan=2, rowspan=1)
# ax2 = plt.subplot2grid((3, 3), loc=(0, 2), colspan=1, rowspan=3)
# ax3 = plt.subplot2grid((3, 3), loc=(1, 0), colspan=2, rowspan=2)
# x = np.arange(1, 10)
# ax1.plot(x, np.exp(x))
# ax2.plot(x, np.log(x))
# ax3.plot(x, pow(x,2))
# plt.show()

# 在一个图中的指定位置插入一个图
# add_axes()

# import matplotlib.pyplot as plt
# import numpy as np
# x = np.arange(0, math.pi*2, 0.05)
# fig = plt.figure()
# ax1 = fig.add_subplot((0.1, 0.1, 0.8, 0.8))
# ax1.plot(x, np.sin(x))
# ax1.set_title('sin(x)')
# ax2 = fig.add_axes((0.55, 0.55, 0.3, 0.3))
# ax2.plot(x, np.cos(x))
# ax2.set_title('cos(x)')
# plt.show()

# add_subplot()
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.arange(0, math.pi*2, 0.05)
# fig = plt.figure()
# ax1 = fig.add_subplot(1,1,1)
# ax1.plot(x, np.sin(x))
# ax1.set_title('sin(x)')
# ax2 = fig.add_subplot(2,2,2,facecolor = 'r')
# ax2.plot(x, np.cos(x), color = 'y')
# ax2.set_title('cos(x)')
# plt.show()

# 网格设置 axes.grid()

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 3, figsize=(10, 5))
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
ax[0].plot(x, pow(x,3))
ax[0].grid(True)  # 展示网格线
ax[1].plot(x, pow(x, 2))
ax[1].grid(color='r', ls='--')  # 展示网格线
plt.show()
