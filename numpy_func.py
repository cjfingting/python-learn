# 字符串函数 numpy.char
# 1.add(数组a,数组b) 	对两个数组的逐个字符串元素进行连接
# import numpy as np
#
# print('连接两个字符串：')
# print(np.char.add(['hello'], [' xyz']))
# print('\n')
#
# print('连接示例：')
# print(np.char.add(['hello', 'hi'], [' abc', ' xyz']))

# 2.multiply(字符串,重复次数) 返回按元素多重连接后的字符串
# print (np.char.multiply('Runoob ',3))

# 3.np.char.center(str , width,fillchar)  str: 字符串，width: 长度，fillchar: 填充字符
# print (np.char.center('Runoob', 20,fillchar = '*'))

# 4.numpy.char.title() 函数将字符串的每个单词的第一个字母转换为大写：
# print (np.char.title('i Like runoob'))

# 5.numpy.char.capitalize() 函数将字符串的第一个字母转换为大写：
# print (np.char.capitalize('runoob'))

# 6.numpy.char.lower() 函数对数组的每个元素转换为小写。
# 操作数组
# print(np.char.lower(['RUNOOB', 'GOOGLE']))
# 操作字符串
# print(np.char.lower('RUNOOB'))

# 7.numpy.char.upper() 函数对数组的每个元素转换为大写
# 操作数组
# print(np.char.upper(['runoob', 'google']))
# 操作字符串
# print(np.char.upper('runoob'))

# 8.numpy.char.split() 通过指定分隔符对字符串进行分割，并返回数组。默认情况下，分隔符为空格
# 分隔符默认为空格
# print(np.char.split('i like runoob?'))
# 分隔符为 .
# print(np.char.split('www.runoob.com', sep='.'))

# 9.numpy.char.splitlines() 函数以换行符作为分隔符来分割字符串，并返回数组。
# 换行符 \n，\r，\r\n 都可用作换行符。
# print(np.char.splitlines('i\nlike runoob?'))
# print(np.char.splitlines('i\rlike runoob?'))

# 10.numpy.char.strip() 函数用于移除开头或结尾处的特定字符。
# 移除字符串头尾的 a 字符
# print(np.char.strip('ashok arunooba', 'a'))
# 移除数组元素头尾的 a 字符
# print(np.char.strip(['arunooba', 'admin', 'java'], 'a'))

# 11.numpy.char.join() 函数通过指定分隔符来连接数组中的元素或字符串
# 操作字符串
# print(np.char.join(':', 'runoob'))
# 指定多个分隔符操作数组元素
# print(np.char.join([':', '-'], ['runoob', 'google']))

# 12.numpy.char.replace() 函数使用新字符串替换字符串中的所有子字符串。
# print(np.char.replace('i like runoob', 'oo', 'cc'))

# 13.numpy.char.encode() 函数对数组中的每个元素调用 str.encode 函数。 默认编码是 utf-8，可以使用标准 Python 库中的编解码器 一维数组
# a = np.char.encode(['runoob','www'], [['cp500','utf-8']])
# print(a)

# 14.numpy.char.decode() 函数对编码的元素进行 str.decode() 解码。
# a = np.char.encode('runoob', 'cp500')
# print(a)
# print(np.char.decode(a, 'cp500'))

# 数学函数
# 1.三角函数:np.sin(),np.cos(),np.tan()
import numpy as np

# a = np.array([0, 30, 45, 60, 90])
# print('不同角度的正弦值：')
# # 通过乘 pi/180 转化为弧度
# print(np.sin(a * np.pi / 180))  # pi即是π
# print('\n')
# print('数组中角度的余弦值：')
# print(np.cos(a * np.pi / 180))
# print('\n')
# print('数组中角度的正切值：')
# print(np.tan(a * np.pi / 180))

# 2.反三角函数 arcsin(),arccos(),arctan()  通过 numpy.degrees() 函数将弧度转换为角度
# a = np.array([0, 30, 45, 60, 90])
# print('含有正弦值的数组：')
# sin = np.sin(a * np.pi / 180)
# print(sin)
# print('\n')
# print('计算角度的反正弦，返回值以弧度为单位：')
# inv = np.arcsin(sin)
# print(inv)
# print('\n')
# print('通过转化为角度制来检查结果：')
# print(np.degrees(inv))
# print('\n')
# print('arccos 和 arctan 函数行为类似：')
# cos = np.cos(a * np.pi / 180)
# print(cos)
# print('\n')
# print('反余弦：')
# inv = np.arccos(cos)
# print(inv)
# print('\n')
# print('角度制单位：')
# print(np.degrees(inv))
# print('\n')
# print('tan 函数：')
# tan = np.tan(a * np.pi / 180)
# print(tan)
# print('\n')
# print('反正切：')
# inv = np.arctan(tan)
# print(inv)
# print('\n')
# print('角度制单位：')
# print(np.degrees(inv))

# 3.numpy.around(a,decimals) 函数返回指定数字的四舍五入值。
# decimals: 舍入的小数位数。 默认值为0。 如果为负，整数将四舍五入到小数点左侧的位置
# a = np.array([1.0, 5.55, 123, 0.567, 25.532])
# print('原数组：')
# print(a)
# print('\n')
# print('舍入后：')
# print(np.around(a))
# print(np.around(a, decimals=1))
# print(np.around(a, decimals=-1))

# 4.numpy.floor() 返回小于或者等于指定表达式的最大整数，即向下取整。
# 5.numpy.ceil() 返回大于或者等于指定表达式的最小整数，即向上取整。
# a = np.array([-1.7, 1.5, -0.2, 0.6, 10])
# print('提供的数组：')
# print(a)
# print('\n')
# print('向上取整后的数组：')
# print(np.ceil(a))
# print ('\n')
# print ('向下取整后的数组：')
# print (np.floor(a))

# 算数函数
# NumPy 算术函数包含简单的加减乘除: add()，subtract()，multiply() 和 divide()。
# 需要注意的是数组必须具有相同的形状或符合数组广播规则。
# import numpy as np
#
# a = np.arange(9, dtype=np.float32).reshape(3, 3)
# print('第一个数组：')
# print(a)
# print('\n')
# print('第二个数组：')
# b = np.array([10, 10, 10])
# print(b)
# print('\n')
# print('两个数组相加：')   +
# print(np.add(a, b))
# print('\n')
# print('两个数组相减：')
# print(np.subtract(a, b))  -
# print('\n')
# print('两个数组相乘：')
# print(np.multiply(a, b)) *
# print('\n')
# print('两个数组相除：')
# print(np.divide(a, b)) /

# numpy.reciprocal() 函数返回参数逐元素的倒数
# import numpy as np
#
# a = np.array([0.25, 1.33, 1, 100])
# print('我们的数组是：')
# print(a)
# print('\n')
# print('调用 reciprocal 函数：')
# print(np.reciprocal(a))

# numpy.power() 函数将第一个输入数组中的元素作为底数，计算它与第二个输入数组中相应元素的幂。 等于** 取幂
# import numpy as np
#
# a = np.array([10, 100, 1000])
# print('我们的数组是；')
# print(a)
# print('\n')
# print('调用 power 函数：')
# print(np.power(a, 2))
# print('\n')
# print('第二个数组：')
# b = np.array([1, 2, 3])
# print(b)
# print('\n')
# print('再次调用 power 函数：')
# print(np.power(a, b))
# print('\n')
# print('调用 **==：')
# print(a ** b)

# numpy.mod() 计算输入数组中相应元素的相除后的余数。 函数 numpy.remainder() 也产生相同的结果。  等于取余%
# import numpy as np
#
# a = np.array([10, 20, 30])
# b = np.array([3, 5, 7])
# print('第一个数组：')
# print(a)
# print('\n')
# print('第二个数组：')
# print(b)
# print('\n')
# print('调用 mod() 函数：')
# print(np.mod(a, b))
# print('\n')
# print('调用 remainder() 函数：')
# print(np.remainder(a, b))
# print('\n')
# print("调用%取余：")
# print(a%b)

# 统计函数
# numpy.amin() 用于计算数组中的元素沿指定轴的最小值。
# numpy.amax() 用于计算数组中的元素沿指定轴的最大值。
# numpy.ptp() 函数计算数组中元素最大值与最小值的差（最大值 - 最小值）
# a: 输入的数组，可以是一个NumPy数组或类似数组的对象。
# axis: 可选参数，用于指定在哪个轴上计算最小值。如果不提供此参数，则返回整个数组的最小值。
# 可以是一个整数表示轴的索引，也可以是一个元组表示多个轴 axis = 0 列比较(可以理解为取出每一行，每行间进行比较) axis = 1 行比较 。
# out: 可选参数，用于指定结果的存储位置。
# keepdims: 可选参数，如果为True，将保持结果数组的维度数目与输入数组相同。如果为False（默认值），则会去除计算后维度为1的轴。
# initial: 可选参数，用于指定一个初始值，然后在数组的元素上计算最小值。
# where: 可选参数，一个布尔数组，用于指定仅考虑满足条件的元素
# import numpy as np
#
# a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
# print('我们的数组是：')
# print(a)
# print('\n')
# print('调用 amin() 函数：')
# print(np.amin(a, 1))
# print('\n')
# print('再次调用 amin() 函数：')
# print(np.amin(a, 0))
# print('\n')
# print('调用 amax() 函数：')
# print(np.amax(a))
# print('\n')
# print('再次调用 amax() 函数：')
# print(np.amax(a, axis=0))
# print ('调用 ptp() 函数：')
# print (np.ptp(a))
# print ('\n')
# print ('沿轴 1 调用 ptp() 函数：')
# print (np.ptp(a, axis =  1))
# print ('\n')
# print ('沿轴 0 调用 ptp() 函数：')
# print (np.ptp(a, axis =  0))

# numpy.percentile(a, q, axis) 百分位数是统计中使用的度量，表示小于这个值的观察值的百分比
# a: 输入数组
# q: 要计算的百分位数，在 0 ~ 100 之间
# axis: 沿着它计算百分位数的轴
# import numpy as np
#
# a = np.array([[10, 7, 4], [3, 2, 1]])
# print('我们的数组是：')
# print(a)
#
# print('调用 percentile() 函数：')
# # 50% 的分位数，就是 a 里排序之后的中位数
# print(np.percentile(a, 50))
#
# # axis 为 0，在纵列上求
# print(np.percentile(a, 50, axis=0))
#
# # axis 为 1，在横行上求
# print(np.percentile(a, 50, axis=1))
#
# # 保持维度不变
# print(np.percentile(a, 50, axis=1, keepdims=True))

# numpy.median(a, axis=None, out=None, overwrite_input=False, keepdims=<no value>)  函数用于计算数组 a 中元素的中位数（中值）
# numpy.mean(a, axis=None, dtype=None, out=None, keepdims=<no value>) 返回数组中元素的算术平均值
# a: 输入的数组，可以是一个 NumPy 数组或类似数组的对象。
# axis: 可选参数，用于指定在哪个轴上计算中位数。如果不提供此参数，则计算整个数组的中位数。可以是一个整数表示轴的索引，也可以是一个元组表示多个轴。
# out: 可选参数，用于指定结果的存储位置。
# overwrite_input: 可选参数，如果为True，则允许在计算中使用输入数组的内存。这可能会在某些情况下提高性能，但可能会修改输入数组的内容。
# keepdims: 可选参数，如果为True，将保持结果数组的维度数目与输入数组相同。如果为False（默认值），则会去除计算后维度为1的轴。
# import numpy as np
#
# a = np.array([[30, 65, 70], [80, 95, 10], [50, 90, 60]])
# print('我们的数组是：')
# print(a)
# print('\n')
# print('调用 median() 函数：')
# print(np.median(a))
# print('\n')
# print('沿轴 0 调用 median() 函数：')
# print(np.median(a, axis=0))
# print('\n')
# print('沿轴 1 调用 median() 函数：')
# print(np.median(a, axis=1))
# print ('\n')
# print ('调用 mean() 函数：')
# print (np.mean(a))
# print ('\n')
# print ('沿轴 0 调用 mean() 函数：')
# print (np.mean(a, axis =  0))
# print ('\n')
# print ('沿轴 1 调用 mean() 函数：')
# print (np.mean(a, axis =  1))

# numpy.average(a, axis=None, weights=None, returned=False) 根据在另一个数组中给出的各自的权重计算数组中元素的加权平均值
# a: 输入的数组，可以是一个 NumPy 数组或类似数组的对象。
# axis: 可选参数，用于指定在哪个轴上计算加权平均值。如果不提供此参数，则计算整个数组的加权平均值。可以是一个整数表示轴的索引，也可以是一个元组表示多个轴。
# weights: 可选参数，用于指定对应数据点的权重。如果不提供权重数组，则默认为等权重。
# returned: 可选参数，如果为True，将同时返回加权平均值和权重总和。
# import numpy as np
#
# a = np.arange(6).reshape(3, 2)
# print('我们的数组是：')
# print(a)
# print('\n')
# print('修改后的数组：')
# wt = np.array([3, 5])
# print(np.average(a, axis=1, weights=wt))
# print('\n')
# print('修改后的数组：')
# print(np.average(a, axis=1, weights=wt, returned=True))

# std = sqrt(mean((x - x.mean())**2))  标准差是一组数据平均值分散程度的一种度量 sqrt代表根号
# var = mean((x - x.mean())** 2) 方差（样本方差）是每个样本值与全体样本值的平均数之差的平方值的平均数
# import numpy as np
#
# print(np.std([1, 2, 3, 4]))
# print (np.var([1,2,3,4]))

# 排序函数
# numpy.sort(a, axis, kind, order)
# a: 要排序的数组
# axis: 沿着它排序数组的轴，如果没有数组会被展开，沿着最后的轴排序(默认按行)， axis=0 按列排序，axis=1 按行排序
# kind: 默认为'quicksort'（快速排序）可选: 'mergesort'（归并排序） 'heapsort'（堆排序）
# order: 如果数组包含字段，则是要排序的字段
# import numpy as np
#
# a = np.array([[3, 7], [9, 1]])
# print('我们的数组是：')
# print(a)
# print('\n')
# print('调用 sort() 函数：')
# print(np.sort(a))
# print('\n')
# print('按列排序：')
# print(np.sort(a, axis=0))
# print('\n')
# # 在 sort 函数中排序字段
# dt = np.dtype([('name', 'S10'), ('age', int)])
# a = np.array([[("raju", 21), ("anil", 25)], [("ravi", 17), ("amar", 27)]], dtype=dt)
# print('我们的数组是：')
# print(a)
# print('\n')
# print('按 name 排序：')
# print(np.sort(a, order='age'))

# numpy.argsort() 函数返回的是数组值从小到大的索引值(即下标)
# import numpy as np
#
# x = np.array([3, 1, 2])
# print('我们的数组是：')
# print(x)
# print('\n')
# print('对 x 调用 argsort() 函数：')
# y = np.argsort(x)  # 输出的是下标
# print(y)
# print('\n')
# print('以排序后的顺序重构原数组：')
# print(x[y])
# print('\n')
# print('使用循环重构原数组：')
# for i in y:
#     print(x[i], end=" ")

# numpy.lexsort() 用于对多个序列进行排序。把它想象成对电子表格进行排序，每一列代表一个序列，排序时优先照顾靠后的列。
# 最后一个键恰好是sort的主键
# import numpy as np
#
# nm = ('raju', 'anil', 'ravi', 'amar')
# dv = ('f.y.', 's.y.', 's.y.', 'f.y.')
# ind = np.lexsort((dv, nm))  # 后一个序列为主
# print('调用 lexsort() 函数：')
# print(ind)
# print('\n')
# print('使用这个索引来获取排序后的数据：')
# print([nm[i] + ", " + dv[i] for i in ind])

# msort(a)	数组按第一个轴排序，返回排序后的数组副本。np.msort(a) 相等于 np.sort(a, axis=0)。
# sort_complex(a)	对复数按照先实部后虚部的顺序进行排序。
# partition(a, kth[, axis, kind, order])	指定一个数，对数组进行分区
# import numpy as np
# a = np.array([3, 2, 4, 1])
# print(a)
# print(np.partition(a, 0))  # 将数组 a 中所有元素（包括重复元素）从小到大排列，3 表示的是排序数组索引为 3 的数字，比该数字小的排在该数字前面，比该数字大的排在该数字的后面
# print(np.partition(a, (1, 3))) # 小于 1 的在前面，大于 3 的在后面，1和3之间的在中间
# argpartition(a, kth[, axis, kind, order])	可以通过关键字 kind 指定算法沿着指定轴对数组进行分区
# import numpy as np
# arr = np.array([46, 57, 23, 39, 1, 10, 0, 120])
# print(np.sort(arr))
# print(np.partition(arr, 3))
# print(arr[np.argpartition(arr, 2)[2]])  # 取第3小的
# print(arr[np.argpartition(arr, 2)[-2]])  # 取第2大的

# np.max(arr,axis)  # 找出给定轴的最大值
# np.min(arr,axis)  # 找出给定轴的最小值
# np.argmax(),np.argmin() # 找出给定轴的的最大值，最小值的索引(下标)
# import numpy as np
#
# a = np.array([[30, 40, 70], [80, 20, 10], [50, 90, 60]])
# print('我们的数组是：')
# print(a)
# print('\n')
# print('调用 argmax() 函数：')
# print(np.argmax(a))
# print('\n')
# print('展开数组：')
# print(a.flatten())
# print('\n')
# print('沿轴 0 的最大值索引：')
# maxindex = np.argmax(a, axis=0)
# print(maxindex)
# print('\n')
# print('沿轴 1 的最大值索引：')
# maxindex = np.argmax(a, axis=1)
# print(maxindex)
# print('\n')
# print('调用 argmin() 函数：')
# minindex = np.argmin(a)
# print(minindex)
# print('\n')
# print('展开数组中的最小值：')
# print(a.flatten()[minindex])
# print('\n')
# print('沿轴 0 的最小值索引：')
# minindex = np.argmin(a, axis=0)
# print(minindex)
# print('\n')
# print('沿轴 1 的最小值索引：')
# minindex = np.argmin(a, axis=1)
# print(minindex)

# numpy.nonzero() 函数返回输入数组中非零元素的索引。
# import numpy as np
#
# a = np.array([[30, 40, 0], [0, 20, 10], [50, 0, 60]])
# print('我们的数组是：')
# print(a)
# print('\n')
# print('调用 nonzero() 函数：')
# print(np.nonzero(a))  # 多维数组，组成原数组的下标

# numpy.where() 函数返回输入数组中满足给定条件的元素的索引。
# import numpy as np
#
# x = np.arange(9.).reshape(3, 3)
# print('我们的数组是：')
# print(x)
# print('大于 3 的元素的索引：')
# y = np.where(x > 3)
# print(y)
# print('使用这些索引来获取满足条件的元素：')
# print(x[y])

# numpy.extract(条件,数组) 函数根据某个条件从数组中抽取元素，返回满条件的元素。
# import numpy as np
#
# x = np.arange(9.).reshape(3, 3)
# print('我们的数组是：')
# print(x)
# # 定义条件, 选择偶数元素
# condition = np.mod(x, 2) == 0
# print('按元素的条件值：')
# print(condition)
# print('使用条件提取元素：')
# print(np.extract(condition, x))  # 默认会展开