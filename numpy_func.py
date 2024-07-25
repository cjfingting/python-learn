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
import numpy as np

a = np.array([10, 100, 1000])
print('我们的数组是；')
print(a)
print('\n')
print('调用 power 函数：')
print(np.power(a, 2))
print('\n')
print('第二个数组：')
b = np.array([1, 2, 3])
print(b)
print('\n')
print('再次调用 power 函数：')
print(np.power(a, b))
print('\n')
print('调用 **==：')
print(a ** b)

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