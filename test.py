"""
多行注释
"""
# 单行注释

# 条件判断
"""
money  = int(input("输入你的钱："))
if money > 600:
    print("enough")
elif money > 400:
    print("a little")
else:
    print("not enough")
"""
# 循环语句 python代码的判断仅仅根据你代码放的位置
# i = 1
# s = 0
# while(i<=100):
#     s = s + i
#     i = i + 1
# print(s)

# for i in range(1,10,2):
#     print(i)

# 转义字符
# print("我是\"你的\"好朋友")
# print("woshi\n你的好朋友")
# print("woshi\\你的好朋友")
# print("woshi\n你的好朋友")
# print(r"woshi\n你的好朋友")
# print(2**3)
# print(not False)
# a = not True
# b = 2 > 1 and 1 < 2
# print(a + b)

# str = 'kiboshing'
# print(str[0:3])
# print(str[-6:-2:6])
# print(str[::-1])

# format函数,count函数，find函数,replace函数，upper函数，lower函数
# str1 = "大家好，我的名字是{0},今年{1}岁，性别{2}".format("haha", "18", "男")
# print(str1.find("haha"))
# print(str1.count("haha"))
# print(str1.replace('ha', 'haha', 2))
# print(str1.upper())
# print(str1)

# # split方法，strip方法
# str2 = '   app ppa '
# print(str2.split('a'))  # 分割函数
# print(str2.strip())  # 去除首尾空格
# print(str2.strip('a'))  # 去除首尾指定字符串
# # 字符串占位符
# print("字符串为:%s" % str2)

# 占位符
# str1 = 'score is %d' % 100
# str2 = 'my name is %s' % 'cj'
# str3 = 'a couple is %s' % [1, 2]
# str4 = 'money is %.3f ' % 999.99
# print(str1)
# print(str2)
# print(str3)
# print(str4)

# f表达式
# name = 'haha'
# age = '18'
# sex = '男'
# str1 = "大家好，我的名字是{0},今年{1}岁，性别{2}".format(name, age, sex)
# print(str1)
# str1 = f'大家好，我的名字是{name},今年{age}岁，性别{sex}'
# print(str1)

# format格式化输出
# print("money is {1:.2f}".format(3.999, 2.9999))
# print("money is {1:.2%}".format(3.999, 2.9999))


# 列表
# 定义列表
# list1 = [2, 3, 4, 'www', [10, 20, 30]]
# list2 = [2, 3, 4]
# # 列表下标：从0开始
# print(list1[4][2])  # 取列表中嵌套的列表的数据
# # 列表长度：
# print(len(list1))
# # 列表更新值,重新赋值
# list1[2] = 'new'
# print(list1 + list2)
# print(list1 * 2)
# print(list1[0:4:2])
# list1.append([1, 2, 3])
# print(list1)
# print(list1.index('aa'))

# 元组操作
# a = set('1234')
# b = set([10, 20, 30])
# c = set((1,2,3,4))
# print(a)
# print(b)
# print(c)
# d = {
#     "年龄":18,
#     "名字":"cj"
# }
# f = set(d)
# print(f)

# 强制类型转化
# a = 123
# print(str(a))
# b = True
# print(str(b))
# c = [1, 2, 3]
# print(str(c))
# d = {1, 2, 3}
# print(str(d))

# print(float("2"))
# print(type(float("2.22")))


# d = {
#     "姓名": 'cj',
#     "年龄": 18,
#     1: 2,
#     (1, 2, 3):'123',
#     "技能": {
#          "技能1": 'python',
#          "技能2": 'java'
#     }
# }
# print(d.items())
# print(d.values())

# for i in range(10):
#     print(i)

# 提取a中的列表中的元素值
a = (1, 2, 3, [10, 20, 30], ['w', 'y', 'z'])
print(a)
for i in a:
    if isinstance(i, list):
         for j in i:
            print(j)

