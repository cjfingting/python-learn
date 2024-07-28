# 饼图只能显示一系列数据，显示的数据为百分比
# matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False,
# labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=0, 0,
# frame=False, rotatelabels=False, *, normalize=None, data=None)
# x：浮点型数组或列表，用于绘制饼图的数据，表示每个扇形的面积。
#
# explode：数组，表示各个扇形之间的间隔，默认值为0。
#
# labels：列表，各个扇形的标签，默认值为 None。
#
# colors：数组，表示各个扇形的颜色，默认值为 None。
#
# autopct：设置饼图内各个扇形百分比显示格式，%d%% 整数百分比，%0.1f 一位小数， %0.1f%% 一位小数百分比， %0.2f%% 两位小数百分比。
#
# pctdistance：：类似于 labeldistance，指定 autopct 的位置刻度，默认值为 0.6。比例值距离圆心的距离
#
# shadow：：布尔值 True 或 False，设置饼图的阴影，默认为 False，不设置阴影。
#
# startangle：：用于指定饼图的起始角度，默认为从 x 轴正方向逆时针画起，如设定 =90 则从 y 轴正方向画起。

# 除此之外，pie() 函数还可以返回三个参数：
# wedges：一个包含扇形对象的列表。
# texts：一个包含文本标签对象的列表。
# autotexts：一个包含自动生成的文本标签对象的列表。
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_axes((0.1, 0.1, 0.8, 0.8))

# 数据
sizes = [15, 30, 45, 10]

# 饼图的标签
labels = ['Java', 'C++', 'C', 'Python']

# 饼图的颜色
colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']

# 突出显示第二个扇形 距离中心距离
explode = (0, 0.1, 0, 0)

# 绘制饼图
ax.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%.2f%%', shadow=True, startangle=90)   # autopct = %.2f%% 两位小数百分比

# 标题
plt.title("RUNOOB Pie Test")

# 显示图形
plt.show()