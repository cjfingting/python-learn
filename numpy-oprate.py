# ndarray数组属性：
# ndim 秩，即轴或维度的数量
# shape 数组的维度，n行m列p维,返回(n,m,p) (p<=2不会显示)
# size 数组元素总个数
# dtype 对象的数据类型
# itemsize 数组中每个元素的大小，以字节为单位
# flags 返回包含有关内存布局的信息，如是否为 C 或 Fortran 连续存储，是否为只读等
import numpy as np

a = np.arange(24)
# print(a.ndim)  # a 现只有一个维度
# 现在调整其大小
b = a.reshape(2, 4, 3)  # b 现在拥有三个维度
# print(b)
# print(b.ndim)
# print(b.shape)

# 切片和索引
# slice(start,stop,step)  切出[start,stop)，步长为step的数组，step默认为1
# arr = np.arange(10)
# arr1 = slice(2,7,2)
# print(arr1)
# 不是用slice方法，也可以使用数组(start:stop:step)的方法切片，多维数组同样，就是把一维数组当成一个元素
# arr1 = arr[2]  # 取下标为2的元素
# arr2 = arr[2:] # 从下标为2切片到最后
# arr3 = arr[2:9]  # 切片arr[2,9)
arr = np.arange(15)
arr.shape = (5,3)
# print(arr)
arr1 = arr[2:4]
# print(arr1)
# ...号代表取当前维度的所有数据，先取出所有数据，然后对另一个维度的数据进行条件取出
arr[...,1]   # 取所有行，取1列
arr[1,...]   # 取所有列，取1行
arr[1:3,...] # 取所有列，取1:3行
arr[...,1:3] # 取所有行，取1:3列
# print(arr)
# print(arr[1,2])  # 取1行2列那个数，就跟正常数组逻辑是一样的
# print(arr[1:,1:]) # 取[1,5),[1,3)的数组

# 高级索引
# 整数数组索引
# arr[[0,1],[0,2]] # 取(0,0),(1,2)的元素拼成数组
# import numpy as np
#
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print('我们的数组是：')
# print(x)
# print('\n')
# rows = np.array([[0, 0], [3, 3]])  # 行标0,0,3,3 中括号控制维度 array创建多维数组
# cols = np.array([[0, 2], [0, 2]])  # 列标0,2,0,2 中括号控制维度 array创建多维数组
# y = x[rows, cols]  # 数组逗号控制维度
# print('这个数组的四个角元素是：')
# print(y)


# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = a[1:3, 1:3]     # 冒号控制连续
# c = a[1:3, [1, 2]]  # 逗号控制序号，数组逗号控制维度
# d = a[..., 1:]      # 省略号表示全部
# print(a)
# print(b)
# print(c)
# print(d)

# 布尔索引  查找满足条件的元素组成数组
# import numpy as np
#
# x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
# print('我们的数组是：')
# print(x)
# print('\n')
# # 现在我们会打印出大于 5 的元素
# print('大于 5 的元素是：')
# print(x[x > 5])


# import numpy as np
#
# a = np.array([1, 2 + 6j, 5, 3.5 + 5j])
# print(a)
# print(a[~np.iscomplex(a)])   # ~ 非运算，取不满足条件的值