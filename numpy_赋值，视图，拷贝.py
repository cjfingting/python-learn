# 1.赋值 不会创建数组对象的副本，使用原始数组的相同id()访问它，使用的是同一个数组，因此，赋值数组改变，原数组也会改变
# import numpy as np
#
# a = np.arange(1, 7)
# b = a
# print(id(a))  # 打印x的地址
# print(a)
# print(b)
# print(id(b))  # 打印x的地址
# b.shape = (3, 2)
# print(b)
# print(a)

# 2，视图或浅拷贝
# 视图是数据的一个别称或引用，通过该别称或引用亦便可访问、操作原有数据，但原有数据不会产生拷贝。如果我们对视图进行修改，它会影响到原始数据，物理内存在同一位置。
# ndarray.view() 方会创建一个新的数组对象，该方法创建的新数组的维数变化不会改变原始数据的维数。
# 使用切片创建视图修改数据会影响到原始数组，但是他们的地址是不同的
# import numpy as np
#
# arr = np.arange(12)
# print('我们的数组：')
# print(arr)
# print('创建切片：')
# a = arr[3:]
# b = arr[3:]
# a[1] = 123
# b[2] = 234
# print(arr)
# print(id(a), id(b), id(arr[3:]))

# ndarray.view() 方会创建一个新的数组对象，该方法创建的新数组的维数变化不会改变原始数据的维数。
# import numpy as np
#
# # 最开始 a 是个 3X2 的数组
# a = np.arange(6).reshape(3, 2)
# print('数组 a：')
# print(a)
# print('创建 a 的视图：')
# b = a.view()
# print(b)
# print('两个数组的 id() 不同：')
# print('a 的 id()：')
# print(id(a))
# print('b 的 id()：')
# print(id(b))
# # 修改 b 的形状，并不会修改 a
# b.shape = 2, 3
# print('b 的形状：')
# print(b)
# print('a 的形状：')
# print(a)

# ndarray.copy() 函数创建一个副本。 对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置。
# import numpy as np
#
# a = np.array([[10, 10], [2, 3], [4, 5]])
# print('数组 a：')
# print(a)
# print('创建 a 的深层副本：')
# b = a.copy()
# print('数组 b：')
# print(b)
# # b 与 a 不共享任何内容
# print('我们能够写入 b 来写入 a 吗？')
# print(b is a)
# print('修改 b 的内容：')
# b[0, 0] = 100
# print('修改后的数组 b：')
# print(b)
# print('a 保持不变：')
# print(a)