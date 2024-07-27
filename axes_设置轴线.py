# 轴尖端是连接轴刻度线的线，划分绘图区域的边界
# 轴对象的尖端位于顶部，底部，左侧和右侧
# 每个尖端可以通过指定颜色和宽度进行格式化
# 如果任何边缘的颜色设置为无，则可以使其不可见
import math
import numpy as np
import matplotlib.pyplot as plt

# fig, axes = plt.subplots(1,2,figsize=(10,4))
# x = np.arange(1,6)
#
# # 原图
# axes[0].plot(x,np.exp(x))
#
# # 设置轴线
# axes[1].plot(x, np.exp(x))
# axes[1].spines['right'].set_visible(False)
# axes[1].spines['top'].set_visible(False)
# axes[1].spines['left'].set_color('r')
# axes[1].spines['bottom'].set_color('y')
# plt.show()

# 格式化轴 通过将axes对象的xscale或vscale属性设置为log，
# 有时还需要在轴编号和轴标签之间显示一些额外的距离，任一轴的labelpad属性都可以设置为所需的值
# fig, axes = plt.subplots(1,2,figsize=(10,4))
# x = np.arange(1,6)
# 原图
# axes[0].plot(x, np.exp(x))
# axes[0].set_xlabel('x value')
# # 设置轴线
# axes[1].plot(x, np.exp(x))
# axes[1].set_yscale('log')  # 将y轴设置为log，则会扩大y轴的范围
# axes[1].set_xlabel('x value')
# axes[1].xaxis.labelpad = 10
# plt.show()

# 设置限制
# fig, axes = plt.subplots(1,2,figsize=(10,4))
# x = np.arange(1,11)
# # 原图
# axes[0].plot(x, np.exp(x))
# # 设置限制
# axes[1].plot(x, np.exp(x))
# axes[1].set_xlim([0,10])  # 设置x轴的范围限制
# axes[1].set_ylim([0,np.exp(x).max()])  # 设置y轴的范围限制
# plt.show()

# 设置刻度和刻度标签
# 刻度表示轴上数据点的标记，可以明确刻度线的位置和标签以满足特定要求
# xticks()和yticks()  将列表对象作为参数，列表中的元素表示将显示刻度的相应操作的位置
# set_xlabels()和set_ylabels()  设置刻度线的标签
# fig, axes = plt.subplots(1,2,figsize=(10, 10))
# x = np.arange(0, math.pi*2, 0.05)
# y = np.sin(x)
#
# # 原图
# axes[0].plot(x,y)
#
# # 设置刻度和刻度标签
# axes[1].plot(x,y)
# axes[1].set_xticks([0, 2, 4, 6])  # 设置刻度
# axes[1].set_xticklabels(['zero', 'two', 'four', 'six'])  # 设置刻度标签
#
# plt.show()

# 设置轴线类型 axis('xxx') tight 原型 equal 等效 off 关闭轴线
# fig, axes = plt.subplots(1,2,figsize=(12, 4))
# x = np.linspace(-1, 1, 100)
# print(x)
# f = lambda x : (1-x**2) ** 0.5  # lambda 函数是一种小型、匿名的、内联函数，它可以具有任意数量的参数，但只能有一个表达式。
#
# # 原图
# axes[0].plot(x, f(x))
# axes[0].plot(x, -f(x))
#
# # 设置轴线类型
# axes[1].plot(x, f(x))
# axes[1].plot(x, -f(x))
# axes[1].axis('equal')
#
# plt.show()

