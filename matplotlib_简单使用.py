import matplotlib
import numpy as np
import math
from matplotlib import pyplot as plt
x = np.arange(0, math.pi*2, 0.05)
zhfont1 = matplotlib.font_manager.FontProperties(fname="SourceHanSansSC-Bold.otf") # 设置中文的格式 默认是无法显示中文的，要下载文件

y = np.sin(x)
plt.plot(x,y)
plt.title("正弦波", fontproperties=zhfont1, color = 'r', fontsize = 14)
plt.xlabel("x轴", fontproperties=zhfont1, color = 'b', fontsize = 10) # x轴标题，颜色，大小
plt.ylabel("y轴", fontproperties=zhfont1, color = 'b', fontsize = 10) # y轴标题，颜色，大小
plt.savefig("sin wave.png")
plt.show()

