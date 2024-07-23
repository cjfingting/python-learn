# b 布尔型 i 整型 u 无符号整型 f 浮点型 c 复数浮点型 m 时间间隔 M 日期时间 O python对象 S 字符串 U unicode V 原始数据
# dtype数据类型对象 即如何自己定义一个数据类型
#         数据类型
#         数据大小
#         数据的字节顺序
# bool b,int,intc,intp,int8 i4,int16 i2,int32 i3 ,int64 i4 ,uint8 u1, uint16 u2,uint32 u3 unit64 u4(无符号整数)
# float f1,float16 f2,float32 f3,float64 f4
# import random

# numpy.tile(数组,reps)
# 在一个平面上将此数组平铺开来（数字对应一维，元组对应二维 tuple（纵铺个数，横铺个数）
import numpy as np

dt = np.dtype('i4')
# 自定义一个数据类型
student = np.dtype([("name", "S20"), ("age", 'u4'), ("mark", 'f4')])
# print(student)
# print(type(student))
# print(dt)
# print(type(dt))

# 创建Ndarray数组对象
# 方法一：
# array(object,dtype,copy,order,subok,ndmin)
# object 数组或嵌套的数列 dtype 数据类型 copy 对象是否复制 order C 行优先 F 列优先 ndmin 最小维度
# 书写方法:中括号包住所有元素，一个元素如果包含多个数据，则用小括号括住 如arr4
# 想用元组作为元素，则dtype = object，python对象，不然无法识别 如arr3
# 一维数组
arr = np.array([1, 2, 3, 4, 5])
# print(arr)
# print(type(arr))

# 元素类型要相同
arr = np.array([1, 2, 2.5, 4])
# print(arr)

# 创建多维数组
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
# print(arr1)

# 规定最小维度
arr2 = np.array([1, 2, 3, 4, 5, 6], ndmin=2)
# print(arr2)

# dtype参数规定数据类型
arr3 = np.array([(1, 2), {3, 4, 5, 6}], dtype=object)
# print(arr3)

# 结构话数据类型
arr4 = np.array([('cj', 18, 32), ('gg', 20, 45)], dtype=student)
# print(arr4)

# 方法二
# asarray(a,dtype,order)函数
# a 可以是列表，列表的元组，元组的元组，元组的列表
# dtype 数据类型
# order C 行优先 F 列优先

# asarray()创建对象
arr = np.asarray((1, 2, 3, 4))
arr1 = np.asarray([1, 2, 3, 4, 5])
arr2 = np.asarray([(1, 2, 3), (1, 2)], dtype=object)

# 方法三
# empty(shape,dtype,order)函数
# shape 数组形状 其他同上
arr = np.empty([3, 2], dtype=int)  # 创建一个3行2列，未初始化的数组(数值不固定)

# 方法四
# zeros(shape,dtype,order)函数 创建指定大小的数组，数组元素用0填充
arr = np.zeros(5, dtype=[('x', 'i4'), ('y', 'S20')])  # 创建一个1行5列的全是0的数组
# print(arr)

# 方法五
# ones(shape,dtype,order)函数 创建指定大小的数组，数组元素用1来填充
arr = np.ones([3, 2], dtype='i4')  # 创建一个3行2列全是1的数组

# 方法六
# full(shape,fill_value,dtype,order)  创建指定大小的数组，数组元素用fill_value来填充
arr = np.full([3, 2], 10, dtype='S')  # 创建一个3行2列全是10的数组
# print(arr)

# 方法七
# eye(N,M,k=0,dtype,order) N 行向量 M 列向量，默认等于行向量 创建一个对角线为1，其他全是0的数组
arr = np.eye(10, dtype='i4')  # 创建一个10行10列的对角线元素为1，其他全是0的一维数组

# 方法八
# arange(start,stop,step,dtype)函数 start 起始值，默认为0，stop 终止值（不包含） step 步长 默认为1
arr = np.arange(stop=10, step=2)  # 创建一个起始值为1，终止值为10，步长为2的一维数组
# print(arr)

# 方法九
# frombuffer(buffer,dtype,count,offset)函数 接受buffer输入参数，流的形式转化为ndarray对象
# buffer 任意对象 count 读取的数据量，默认全部 offset 读取的起始位置，默认为0
# 如果输入字符串则要在输入的字符串前加一个b
s = b'cj is a good man'
arr = np.frombuffer(s, dtype='S1')
# print(arr)

# 方法十
# fromiter(iterable,dtype,count) iterable 可迭代对象 dtype必须指定，没有默认值
x = [1, 2, 3, 4]
z = iter(x)  # 转化为一个可迭代对象
arr = np.fromiter(z, dtype='f')
# print(arr)

# 方法十一
# linspace(start,stop,num=50,endpoint=True,retstep=False,dtype=None) 创建一个一维数组，由等差数列构成
# start 序列起始值 stop 序列终止值，当endpoint为真，则包含此值 num 样本数量，默认50 retstep为真，数组会显示间距
arr = np.linspace(1, 10, 10, dtype='i1')
# print(arr)

# 方法十二
# logspace(start,stop,num=50,endpoint=True,base=10,dtype=None)
# 序列起始值 base*start 序列终止值 base*stop 当endpoint为真，则包含此值 num 样本数量，默认50 base 对数log的底数，默认是10
arr = np.logspace(1, 10, 10, dtype='i4', base=2)
# print(arr)

# 方法十三
# random.rand(x,y,z) 生成x行y列z维的[0,1)的随机数(x，y，z都可省略)
arr = np.random.rand(3,2,3)
# print(arr)

# 方法十四
# random.random(x) 生成x个的[0,1)的随机数(x可省略)
arr = np.random.rand(3)

# 方法十五
# random.randint(low,high,size=None,dtype=‘i') low 包含的下限，high 不包含的上限 size 元素个数,默认为1
arr = np.random.randint(1,10)
# print(arr)

# 方法十六
# random.randn(x,y,z)  返回生成x行y列z维满足正态分布的随机数(x，y，z都可省略)
arr = np.random.rand(3,2,3)
# print(arr)

# 方法十七
# random.normal(loc-0.0,scale=1.0,size=None) 生成高斯分布的概率密度的随机数
# loc 浮点型 概率分布的均值 scale 浮点型，概率分布的标准差 size 输出的个数，默认一个
arr = np.random.normal(1.0,1.0,5)
print(arr)


