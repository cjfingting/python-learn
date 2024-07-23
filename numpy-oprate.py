# ndarray数组属性：
# ndim 秩，即轴或维度的数量
# shape 数组的维度，n行m列p维,返回(n,m,p) (p<=2不会显示)
# size 数组元素总个数
# dtype 对象的数据类型
# itemsize 数组中每个元素的大小，以字节为单位
# flags 返回包含有关内存布局的信息，如是否为 C 或 Fortran 连续存储，是否为只读等
# 数组的装置 数组.T 数组转置并不会改变内存存储
# 数组的复制 数组.copy(order='C')
# order：可选参数，'C’表示按行顺序（C风格）；'F’表示按列顺序（Fortran风格）；'A’表示原顺序，'E’表示元素顺序。
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

# 广播 对不同形状的数组进行数值计算的方式
# 形状相同：如果形状相同，那么对数组的算术运算通常在相应的元素上进行
# import numpy as np
#
# a = np.array([1, 2, 3, 4])
# b = np.array([10, 20, 30, 40])
# c = a * b
# print(c)

# 形状不同 触发广播规则
# 要求： 有一个数组是一维（行）的   一维的数组与多维的数组列数要相同
# import numpy as np
#
# a = np.array([[0, 0, 0],
#               [10, 10, 10],
#               [20, 20, 20],
#               [30, 30, 30]])
# b = np.array([0, 0, 0])
# print(a + b)

# 迭代数组，访问数组所有元素  numpy.nditer(数组,order = 'F/C',op_flags=['read-only'],flags = ['external_loop'])
# 按照内存布局顺序输出，默认行优先
# order 可选参数，读的方式
# op_flags 可选参数，权限控制 read-only 只读 readwrite 读写 writeonly 只写
# flags 可选参数  c_index	可以跟踪 C 顺序的索引 f_index	可以跟踪 Fortran 顺序的索引 multi_index	每次迭代可以跟踪一种索引类型 external_loop	给出的值是具有多个值的一维数组，而不是零维数组

import numpy as np
a = np.arange(0,60,5)
a = a.reshape(3,4)
print ('原始数组是：')
print (a)
print ('\n')
print ('修改后的数组是：')
# for x in np.nditer(a):
#     print(x, end=", ")  # end表示在后面加啥
# print('\n')
# for x in np.nditer(a, op_flags=['readwrite']):
#     x[...] = 2 * x
# print('修改后的数组是：')
# print(a)
#
# for x in np.nditer(a, flags =  ['c_index'], order =  'F'):
#    print (x, end=", " )
#
# for x in np.nditer(a, flags =  ['f_index'], order =  'F'):
#    print (x, end=", " )

# for x in np.nditer(a, flags =  ['external_loop']):
#    print (x, end=", " )  # 一起全部读完，所有放在一个数组
#
# print('\n')
#
# for x in np.nditer(a, flags =  ['external_loop'], order =  'F'):
#     print (x, end=", " ) # 读完一列是一个数组

# 广播迭代
# 如果两个数组是可广播的，nditer 组合对象能够同时迭代它们。
# 假设数组 a 的维度为 3X4，数组 b 的维度为 1X4 ，则使用以下迭代器（数组 b 被广播到 a 的大小）。
# import numpy as np
#
# a = np.arange(0, 60, 5)
# a = a.reshape(3, 4)
# print('第一个数组为：')
# print(a)
# print('\n')
# print('第二个数组为：')
# b = np.array([1, 2, 3, 4], dtype=int)
# print(b)
# print('\n')
# print('修改后的数组为：')
# for x, y in np.nditer([a, b]):
#     print("%d:%d" % (x, y), end=", ")

# 修改数组形状
# reshape(shape,order = 'C')
# shape:整数或者整数数组，新的形状应当兼容原有形状(行,列) order = C 按行 F 按列 A 原顺序 k 内存中出现顺序
# import numpy as np
#
# a = np.arange(8)
# print('原始数组：')
# print(a)
# print('\n')
#
# b = a.reshape(4, 2)
# print('修改后的数组：')
# print(b)

# flat 数组元素迭代器
# import numpy as np
#
# a = np.arange(9).reshape(3, 3)
# print('原始数组：')
# for row in a:
#     print(row)
#
# # 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
# print('迭代后的数组：')
# for element in a.flat:
#     print(element)

# flatten(order='C') 展平的数组元素并拷贝一份，修改返回的数组，不会对原数组产生影响
# order = C 按行 F 按列 A 原顺序 k 内存中出现顺序
# import numpy as np
#
# a = np.arange(8).reshape(2, 4)
#
# print('原数组：')
# print(a)
# print('\n')
# # 默认按行
#
# print('展开的数组：')
# print(a.flatten())
# print('\n')
#
# print('以 F 风格顺序展开的数组：')
# print(a.flatten(order='F'))

# ravel(order='C') 展平的数组元素，返回的是数组视图，按C风格修改会影响原始数组，按F风格修改不会影响原始数组
# import numpy as np
#
# a = np.arange(8).reshape(2, 4)
#
# print('原数组：')
# print(a)
# print('\n')
#
# print('调用 ravel 函数之后：')
# print(a.ravel())
# print('\n')
#
# print('以 F 风格顺序调用 ravel 函数之后：')
# print(a.ravel(order='F'))

#