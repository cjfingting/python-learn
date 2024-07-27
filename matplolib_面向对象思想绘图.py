# Figure类  matplotlib.figure模块包含Figure类，它是所有plot元素的顶级容器，通过从pyplot模块调用figure()函数来实例Figure对象
# Axes类  Axes对象是具有数据空间的图像区域，给定的图形可以包含许多轴，但是给定的Axes对象只能在一个图中
# figure对象通过调用add.axes(左,底,宽,高)方法将Axes对象添加到图中
# ax.legend(labels,loc) 为绘图图形添加图例 labels 描述 loc 位置
# best 正上方 upper right/upper left/lower left/lower right/right/center left/center right/lower center/upper center/center
# ax.plot 将一个数组的值与另一个数组的值绘制为线或标记
# ax.plot(x,y,[fmt])
# fmt包含参数颜色，点标记，线条样式
# 颜色
# 'b'	蓝色
# 'g'	绿色
# 'r'	红色
# 'c'	青色
# 'm'	品红色
# 'y'	黄色
# 'k'	黑色
# 'w'	白色

# 点标记
# . 点标记
# , 像素
# o 圆形
# v 朝下三角形
# ^ 朝上三角形
# < 朝左三角形
# > 朝右三角形
# s 正方形
# p 五角星
# * 星型
# h 1号六角形
# H 2号六角形
# + +号标记
# D 钻石型
# d 小版钻石型
# | 垂直线性
# - 水平线型

# 线条样式
# - 实线
# -- 虚线
# -. 单点画线
# : 点虚线

# 更多属性
# color 颜色
# alpha 透明度
# ls    线型
# lw    线宽
# marker 点类型
# markersize 点大小
# markeredgewidth 点边缘宽度
# markeredgecolor 点边缘颜色
# markerfacecolor 点内部严肃
import matplotlib.pyplot as plt
import math
import numpy as np
import matplotlib

zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf") # 设置中文的格式 默认是无法显示中文的，要下载文件
fig = plt.figure()  # 图形的顶级容器，那张大白纸
x = np.arange(0, math.pi * 2, 0.05)
y1 = np.sin(x)
y2 = np.cos(x)
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))  # 大画布分一块出来用于画一个图，在ax模块画图
ax.set_title('函数比较', fontproperties=zhfont1) # 设置标题
ax.plot(x, y1, color='r', alpha=0.5, ls='-', lw=5)  # Axes对象才是真正画图的地方
ax.plot(x, y2, "r--", markersize=3)
ax.legend(["sin", "cos"], loc="lower right")
plt.show()  # 展示图形
