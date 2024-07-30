# 图像灰度化  R = G = B
# 最小值法或者最大值法
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
# data = mpimg.imread('ganyu.jpg')
# print(data.shape)
# # print(data)
# data_gray = data.min(axis=-1)   # 最小值法
# data_gray = data.max(axis=-1)   # 最小值法
# data_gray = data.mean(axis=-1)  # 平均值法
# print(data_gray.shape)
# plt.imshow(data_gray,cmap='gray')
# plt.show()

# 加权平均值法  常用
data = mpimg.imread('ganyu.jpg')
rgb_weight = [0.299,0.384,0.114,0.203]   # 权重
data_grey = np.dot(data,rgb_weight)
plt.imshow(data_grey,cmap='gray')
plt.show()
