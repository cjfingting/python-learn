# pillow模块处理图片
# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt
# ganyu = Image.open('C:/Users/cj/OneDrive/图片/屏幕快照/2022-04-14 (2).png')
# ganyu_data = np.array(ganyu)
# # 红绿蓝 -> 绿红蓝
# ganyu_data = ganyu_data[:,:,[1, 0, 2]]
#
# print(ganyu_data)
# plt.imshow(ganyu_data)
# plt.axis('off')
# plt.show()

# matplotlib包中的图像模块  仅支持PNG图像
# imread() 用于float32 dtype的ndarray对象中的图像数据 正确读取应该是0-1直接的浮点数
# imshow() 展示图片，可加入各种参数
# imsave() 保存图片
# import numpy as np
# import matplotlib.image as mpimg
# import matplotlib.pyplot as plt
#
# data = mpimg.imread('ganyu.jpg')  # 读取成功是因为直接改后缀了，内部逻辑其实还是PNG
# data = data[:, :, 0]  # 变成二维了
# # print(type(data))
# print(data)
# plt.imshow(data, cmap='hot')
# plt.set_cmap("nipy_spectral")
# plt.colorbar(ticks=[0.1, 0.2, 0.3, 0.4, 0.5], orientation='horizontal')
# plt.axis('off')
# plt.imsave('ganyu.png', data, cmap='grey')
# plt.show()

# 3.ndarray图像操作
# 旋转图片
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt

arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
                [[13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24]],
                [[24, 25, 26], [27, 28, 29], [30, 31, 32], [33, 34, 35]]])
# print(arr[::, ::-1, ::])  # 横行进行交换，即进行图片左右交换  高 宽 色
# data = mpimg.imread('ganyu.jpg')
# data = data[::-1, ::,::]   # 图片上下交换
# data = data[::, ::-1, ::]  # 图片左右交换
# plt.imshow(data)
# plt.show()

# 图片打码
data = mpimg.imread('ganyu.jpg')
data_temp = data[250:1570,1500:2500]  # 裁剪图片
data_temp = data_temp[::20,::20]  # 隔20个拿一个像素点，相当于马赛克
for i in range(66):
    for j in range(50):   # 将取出的像素点一个个替换
        data[250+20*i:250+20+i*20,1500+20*j:1500+20+20*j] = data_temp[i][j]
plt.imshow(data)
plt.show()

# 图片拼接
data1 = mpimg.imread('ganyu.jpg')
data2 = np.concatenate([data1,data1],axis=0)  # 列拼接
data2 = np.concatenate([data1,data1],axis=1)  # 行拼接

# 图片切割
data = mpimg.imread('ganyu.jpg')
data1,data2,data3 = np.split(data,indices_or_sections=[300,500],axis=1) # 300之前一个，300-500一个，500之后一个