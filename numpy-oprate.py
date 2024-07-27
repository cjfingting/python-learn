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
arr.shape = (5, 3)
# print(arr)
arr1 = arr[2:4]
# print(arr1)
# ...号代表取当前维度的所有数据，先取出所有数据，然后对另一个维度的数据进行条件取出
arr[..., 1]  # 取所有行，取1列
arr[1, ...]  # 取所有列，取1行
arr[1:3, ...]  # 取所有列，取1:3行
arr[..., 1:3]  # 取所有行，取1:3列
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

# import numpy as np
# a = np.arange(0,60,5)
# a = a.reshape(3,4)
# print ('原始数组是：')
# print (a)
# print ('\n')
# print ('修改后的数组是：')
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
# shape:整数或者整数数组，新的形状应当兼容原有形状(行,列) order = C 按行 F 按列 A 原顺序 k 内存中出现顺序，行列中有一个可以为-1，由总数/已确定的行(列)
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

# 翻转数组
# transpose(数组,axes=None)  axes对应维度,通畅所有维度都会对换，即数组转置

# a = np.arange(12).reshape(3, 4)
#
# print('原数组：')
# print(a)
# print('\n')
#
# print('对换数组：')
# print(np.transpose(a))

# ndarray.T 数组转置
# import numpy as np
#
# a = np.arange(12).reshape(3, 4)
#
# print('原数组：')
# print(a)
# print('\n')
#
# print('转置数组：')
# print(a.T)

# numpy.rollaxis(a,axis,start=0) axis 要向后滚动的轴，其他轴的相对位置不会改变 start 默认为0，表示完整的滚动
# 就是轴axis替换start位置，对应的位置向后移 axis > start
# import numpy as np
# a = np.arange(24).reshape(4,2,3)  # 3为深度，即二维数组的数量，2,3为行列
# print(a)
# print(np.rollaxis(a,2))  # 从深度转化则要跨维度找数，组成后面的m行n列
# print(np.rollaxis(a,2,1)) # 从后面转化，则就是数组转置

# swapaxes(a,axis1,axis2) 交换数组的两个轴
# print((np.swapaxes(a,2,0)))

# 修改数组维度
# # broadcast(x,y) 它返回一个对象，该对象封装了将一个数组广播到另一个数组的结果,对y广播x
# import numpy as np
#
# x = np.array([[1], [2], [3]])
# y = np.array([4, 5, 6])
#
# # 对 y 广播 x 即将y变成x的维度
# b = np.broadcast(x, y)
# # 它拥有 iterator 属性，基于自身组件的迭代器元组
#
# print('对 y 广播 x：')
# r, c = b.iters
#
# # Python3.x 为 next(context) ，Python2.x 为 context.next()
# print(next(r), next(c))
# print(next(r), next(c))
# print('\n')
# # shape 属性返回广播对象的形状
#
# print('广播对象的形状：')
# print(b.shape)
# print('\n')
# # 手动使用 broadcast 将 x 与 y 相加
# b = np.broadcast(x, y)
# c = np.empty(b.shape)
#
# print('手动使用 broadcast 将 x 与 y 相加：')
# print(c.shape)
# print('\n')
#
# print('x 与 y 的和：')
# print(x + y)

# broadcast_to(array,shape,subok=False) 返回一个只读视图，shape要满足广播规则，即列不能改变
# import numpy as np
#
# a = np.arange(4).reshape(1, 4)
#
# print('原数组：')
# print(a)
# print('\n')
#
# print('调用 broadcast_to 函数之后：')
# print(np.broadcast_to(a, (4, 4)))

# expand_dims(arr,axis=None) 通过在指定位置插入新的轴来扩展数组形状,插入轴其实就是增加维度，shape对应的位置(深度，高度，宽度)
# import numpy as np
#
# x = np.array(([1, 2], [3, 4]))
#
# print('数组 x：')
# print(x)
# print('\n')
# y = np.expand_dims(x, axis=0)  （2,2) -> (1,2,2)
#
# print('数组 y：')
# print(y)
# print('\n')
#
# print('数组 x 和 y 的形状：')
# print(x.shape, y.shape)
# print('\n')
# # 在位置 1 插入轴
# y = np.expand_dims(x, axis=1)
#
# print('在位置 1 插入轴之后的数组 y：')
# print(y)
# print('\n')
#
# print('x.ndim 和 y.ndim：')
# print(x.ndim, y.ndim)
# print('\n')
#
# print('x.shape 和 y.shape：') (2,2) -> (2,1,2)
# print(x.shape, y.shape)

# squeeze(arr,axis) 从给定数组的形状中删除一堆的条目 axis 删除轴的位置 只能删除值为1的轴的位置，不然不是报错就是无作用
# 纯就是降维度的作用
# import numpy as np
#
# x = np.arange(9).reshape(3, 1, 3)
#
# print('数组 x：')
# print(x)
# print('\n')
# y = np.squeeze(x,1)
# print('数组 y：')
# print(y)
# print('\n')
#
# print('数组 x 和 y 的形状：')
# print(x.shape, y.shape)

# 连接数组
# concatenate((a1,a2,a3...),axis) 用于沿指定轴连接相同形状的两个或多个数组
# a1,a2,a3...相同类型的数组 axis 沿着它连接数组的轴
# import numpy as np
#
# a = np.array([[1, 2], [3, 4]])
#
# print('第一个数组：')
# print(a)
# print('\n')
# b = np.array([[5, 6], [7, 8]])
#
# print('第二个数组：')
# print(b)
# print('\n')
# # 两个数组的维度相同
#
# print('沿轴 0 连接两个数组：')
# print(np.concatenate((a, b)))
# print('\n')
#
# print('沿轴 1 连接两个数组：')
# print(np.concatenate((a, b), axis=1))

# stack((arr1,arr2..),axis) axis 返回数组中的轴，输入数组沿着它来堆叠 主要目的就是升维度
# import numpy as np
#
# a = np.array([[1, 2], [3, 4]])
#
# print('第一个数组：')
# print(a)
# print('\n')
# b = np.array([[5, 6], [7, 8]])
#
# print('第二个数组：')
# print(b)
# print('\n')
#
# print('沿轴 0 堆叠两个数组：')
# print(np.stack((a, b), 0))
# print('\n')
#
# print('沿轴 1 堆叠两个数组：')
# print(np.stack((a, b), 1))

# hstack((arr1,arr2..))通过水平堆叠来生成数组,不升维度
# vstack((arr1,arr2..))通过竖直堆叠来生成数组,不升维度
# import numpy as np
#
# a = np.array([[1, 2], [3, 4]])
#
# print('第一个数组：')
# print(a)
# print('\n')
# b = np.array([[5, 6], [7, 8]])
#
# print('第二个数组：')
# print(b)
# print('\n')
#
# print('水平堆叠：')
# c = np.hstack((a, b))
# print(c)
# print('\n')
#
# print('垂直堆叠：')
# d = np.vstack((a, b))
# print(d)
# print('\n')

# numpy.split(arr,indices_or_sections,axis=0)
# indices_or_sections是一个整数，就用该数平均切分，如果是一个数组，为沿轴切分的位置 (必须参数)
# 沿着哪个维度进行切分，默认为0，横向切分，为1时，纵向切分,这个参数只在多维数组有用
# import numpy as np
#
# a = np.arange(9)
#
# print('第一个数组：')
# print(a)
# print('\n')
#
# print('将数组分为三个大小相等的子数组：')
# b = np.split(a, 3)
# print(b)
# print('\n')
#
# print('将数组在一维数组中表明的位置分割：')
# b = np.split(a, [4, 7])  # 下标为4和7的地方切两刀
# print(b)

# hsplit() 用于水平分割数组，通过指定要返回的相同形状的数组数量来拆分原数组，相当于上述的axis=1
# import numpy as np
#
# harr = np.floor(10 * np.random.random((2, 6)))
# print('原array：')
# print(harr)
#
# print('拆分后：')
# print(np.hsplit(harr, 3))

# vsplit() 沿着垂直轴分割，其分割方式与hsplit用法相同,相当于上述的axis=0

# 数组元素的添加与删除
# resize(arr,shape) shape：返回数组的新形状
# 函数返回指定大小的新数组
# 如果新数组大小大于原始大小，则包含原始数组中的元素的副本,就是把元素疯狂重用
# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6]])
#
# print('第一个数组：')
# print(a)
# print('\n')
#
# print('第一个数组的形状：')
# print(a.shape)
# print('\n')
# b = np.resize(a, (3, 2))
#
# print('第二个数组：')
# print(b)
# print('\n')
#
# print('第二个数组的形状：')
# print(b.shape)
# print('\n')
# # 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了
#
# print('修改第二个数组的大小：')
# b = np.resize(a, (3, 4))
# print(b)

# numpy.append(arr,value,axis=None) 返回一个新数组
# value 要想arr添加的值，需要和arr形状相同，输入数组的维度必须匹配 (追加数组)
# axis 默认为 None。当axis无定义时，是横向加成，返回总是为一维数组！则上述value值随便输入
# 当axis有定义的时候，分别为0和1的时候。当axis为0时,数组时加在下边（列数要相同）。
# 当axis为1时，数组是加在右边（行数要相同）
# import numpy as np
#
# a = np.array([[1, 2, 3], [4, 5, 6]])
#
# print('第一个数组：')
# print(a)
# print('\n')
#
# print('向数组添加元素：')
# print(np.append(a, 7))
# print('\n')
#
# print('向数组添加元素：')
# print(np.append(a, [7, 8, 9]))
# print('\n')
#
# print('沿轴 0 添加元素：')
# print(np.append(a, [[7, 8, 9]], axis=0))
# print('\n')
#
# print('沿轴 1 添加元素：')
# print(np.append(a, [[5, 5], [7, 8]], axis=1))    #  将前一个元素作为一行而不是一列

# numpy.insert(arr,obj,value,axis) 在给定索引之前，沿给定轴在输入数组中插入值
# arr：输入数组
# obj：在其之前插入值的索引
# values：要插入的值 可插入多个值，用数组包起来
# axis：沿着它插入的轴，如果未提供，则输入数组会被展开 0 表示行 1 表示列
# import numpy as np
#
# a = np.array([[1, 2], [3, 4], [5, 6]])
#
# print('第一个数组：')
# print(a)
# print('\n')
#
# print('未传递 Axis 参数。 在删除之前输入数组会被展开。')
# print(np.insert(a, 3, [11, 12]))
# print('\n')
# print('传递了 Axis 参数。 会广播值数组来配输入数组。')
#
# print('沿轴 0 广播：')
# print(np.insert(a, 1, [11], axis=0))
# print('\n')
#
# print('沿轴 1 广播：')
# print(np.insert(a, 1, [[11], [12]], axis=1)) # 最外面的中括号表示数组，一个中括号表示一行，中括号里面表示元素

# numpy.delete(arr,obj,axis) 不会改变原数组
# arr：输入数组
# obj：可以被切片，整数或者整数数组，表明要从输入数组删除的子数组
# axis：沿着它删除给定子数组的轴，如果未提供，则输入数组会被展开 0 表示行 1 表示列
# import numpy as np
#
# a = np.arange(12).reshape(3, 4)
#
# print('第一个数组：')
# print(a)
# print('\n')
#
# print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
# print(np.delete(a, 5))
# print('\n')
#
# print('删除第二列：')
# print(np.delete(a, 1, axis=1))
# print('\n')
#
# print('包含从数组中删除的替代值的切片：')
# a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(np.delete(a, np.s_[::2]))

# numpy.unique(arr,return_index,return_inverse,return_counts)
# arr：输入数组，如果不是一维数组则会展开
# return_index：如果为true，返回新列表元素在旧列表中的位置（下标），并以列表形式储
# return_inverse：如果为true，返回旧列表元素在新列表中的位置（下标），并以列表形式储
# return_counts：如果为true，返回去重数组中的元素在原数组中的出现次数
# import numpy as np
#
# a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
#
# print('第一个数组：')
# print(a)
# print('\n')
#
# print('第一个数组的去重值：')
# u = np.unique(a)
# print(u)
# print('\n')
#
# print('去重数组的索引数组：')
# u, indices = np.unique(a, return_index=True)
# print(indices)
# print('\n')
#
# print('我们可以看到每个和原数组下标对应的数值：')
# print(a)
# print('\n')
#
# print('去重数组的下标：')
# u, indices = np.unique(a, return_inverse=True)
# print(u)
# print('\n')
#
# print('下标为：')
# print(indices)
# print('\n')
#
# print('使用下标重构原数组：')
# print(u[indices])
# print('\n')
#
# print('返回去重元素的重复数量：')
# u, indices = np.unique(a, return_counts=True)
# print(u)
# print(indices)
