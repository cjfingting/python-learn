# 1.条形图
# 垂直条形图 ax.bar(x,height,width=0.8,bottom=None,align='center',color)
# x 条形的x坐标的标量序列
# height 标量或标量序列表示条的高度
# width 标量或类似数组，可选
# bottom 标量或类似数组 y轴最小值 可选
# align center/edge 可选
# color 颜色
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
# ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
# langs = ['C', 'C++', 'Python', 'Java']
# student = [22, 33, 44, 55]
# ax.bar(langs, student,0.5, align='center',color='r')
# plt.show()

# 条形组合条形图
# ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
# langs = ['C', 'C++', 'Python', 'Java']
# print(len(langs))
# len = np.arange(len(langs))
# print(len)
# data = [[22, 33, 44, 55],
#         [23, 34, 45, 56]]
# ax.bar(len, data[0], 0.05, align='center',color='r')  # 数据只能一组一组的传，不能一次性传多维数组
# # 平移只能用数字，因此要将字符串列表转换为数字，然后再用label转换回去
# ax.bar(len+0.05, data[1], 0.05, align='center',color='b')  # 数据只能一组一组的传，不能一次性传多维数组
# ax.set_xticks(len)  # 设置刻度线
# ax.set_xticklabels(langs)  # 设置刻度标签
# plt.show()

# 垂直堆叠条形图 表示彼此顶部的不同组的条形图 条形图的高度显示组的组合结果
# ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
# N = 5
# ind = np.arange(1, N+1)
# menNum = [20,30,40,50,60]
# womenNum = [25,35,45,55,65]
# ax.bar(ind, womenNum, color='blue')
# ax.bar(ind, menNum, color='red', bottom=womenNum)  # 这个数据在上一个数据上面堆叠上去
# ax.set_xticks(ind)
# ax.set_xticklabels(['C','D','E','F','G'])
# ax.legend(["women", "men"], loc="upper left")
# plt.show()

# 水平条形图 ax.barh(y,height=0.8,width,bottom=None,align='center',color)
# y 条形的y坐标的标量序列
# height 标量或标量序列表示条的宽度
# width 标量或类似数组，可选
# bottom 标量或类似数组 y轴最小值 可选
# align center/edge 可选
# color 颜色
# ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
# langs = ['C', 'C++', 'Python', 'Java']
# student = [22, 33, 44, 55]
# ax.barh(langs, student,0.5, align='center',color='r')
# plt.show()

ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))
langs = ['C', 'C++', 'Python', 'Java']
print(len(langs))
len = np.arange(len(langs))
print(len)
data = [[22, 33, 44, 55],
        [23, 34, 45, 56]]
ax.barh(len, data[0], 0.2, align='center',color='r')  # 数据只能一组一组的传，不能一次性传多维数组
# 平移只能用数字，因此要将字符串列表转换为数字，然后再用label转换回去
ax.barh(len+0.2, data[1], 0.2, align='center',color='b')  # 数据只能一组一组的传，不能一次性传多维数组
ax.set_yticks(len)  # 设置刻度线
ax.set_yticklabels(langs)  # 设置刻度标签
plt.show()

