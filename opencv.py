import cv2
import numpy as np

img = cv2.imread('ganyu.jpg')
print(img)  # 图片的读取shape为h,w,c h 高度 w 宽度  c RGB三原色 h,w定位像素点，c 行 列 维
# cv2.imshow('ganyu.jpg', img[200:500,0:200])
# cv2.waitKey(0)
print(img.shape)
B = img[0, :, 0]
print(B)

# a = np.arange(24).reshape(2, 3, 4)
# print(a)
# print(a[0, 0, :])
