# b 布尔型 i 整型 u 无符号整型 f 浮点型 c 复数浮点型 m 时间间隔 M 日期时间 O python对象 S 字符串 U unicode V 原始数据
# dtype数据类型对象 即如何自己定义一个数据类型
#         数据类型
#         数据大小
#         数据的字节顺序
# bool b,int,intc,intp,int8 i4,int16 i2,int32 i3 ,int64 i4 ,uint8 u1, uint16 u2,uint32 u3 unit64 u4(无符号整数)
# float f1,float16 f2,float32 f3,float64 f4
import numpy as np

dt = np.dtype('i4')
# 自定义一个数据类型
student = np.dtype([("name", "S20"), ("age", 'u4'), ("mark", 'f4')])
print(student)
print(type(student))
print(dt)
print(type(dt))

# 创建Ndarray数组对象
# 方法一：
# array(object,dtype,copy,order,subok,ndmin)
# object 数组或嵌套的数列 dtype 数据类型 copy 对象是否复制 order C 行优先 F 列优先 ndmin 最小维度
# 书写方法:中括号包住所有元素，一个元素如果包含多个数据，则用小括号括住 如arr4
# 想用元组作为元素，则dtype = object，python对象，不然无法识别 如arr3
# 一维数组
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# 元素类型要相同
arr = np.array([1, 2, 2.5, 4])
print(arr)

# 创建多维数组
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)

# 规定最小维度
arr2 = np.array([1, 2, 3, 4, 5, 6], ndmin=2)
print(arr2)

# dtype参数规定数据类型
arr3 = np.array([(1, 2), {3, 4, 5, 6}], dtype=object)
print(arr3)

# 结构话数据类型
arr4 = np.array([('cj', 18, 32), ('gg', 20, 45)], dtype=student)
print(arr4)

# 方法二
# asarray(a,dtype,order)函数
# a 可以是列表，列表的元组，元组的元组，元组的列表
# dtype 数据类型
# order C 行优先 F 列优先

# asarray()创建对象
arr = np.asarray((1, 2, 3, 4))
arr1 = np.asarray([1, 2, 3, 4, 5])
arr2 = np.asarray([(1, 2, 3), (1, 2)],dtype=object)

# 方法三
# empty(shape,dtype,order)函数
# shape 数组形状 其他同上
arr = np.empty([3,2],dtype = int) # 创建一个3行2列，未初始化的数组