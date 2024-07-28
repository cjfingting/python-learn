# 轮廓图是一种在二位平面上显示三维表面的方法，它绘制了y轴上的两个预测变量X Y和轮廓的响应变量Z
# 自变量X和Y通常限于称为meshgrid的规则网络；numpy.meshgrid使用x值数组和y值数组创建一个矩形网络
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)
x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = np.sqrt(X ** 2 + Y ** 2)
con = ax.contour(X, Y, Z,cmap='afmhot_r')
plt.show()
