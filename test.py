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

# split方法，strip方法
str2 = '   app ppa '
print(str2.split('a'))  # 分割函数
print(str2.strip())  # 去除首尾空格
print(str2.strip('a'))  # 去除首尾指定字符串


