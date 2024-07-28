# text()  在axes对象的任意位置添加文字
# xlabel() 为x轴添加标签
# ylabel() 为y轴添加标签
# title()  为axes对象添加标题
# legend() 为axes对象添加图例
# suptitle() 为figure对象添加中心化的标题
# figtext()  在figure对象的任意位置添加文字
# annotate(xy,xytext,arrowprops) 为axes对象添加注释(箭头可选)
# xy 箭头指示位置 xytext 注释文字的位置 arrowprops 以字典的形式设置箭头的样式
# 箭头样式 width 箭头长方形部分的宽度 headlength 设置箭头尖端的长度 headwidth 箭头尖端底部的宽度 facecolor 箭头颜色 shrink 箭头顶点，尾部与指示点、注释文字的距离
# 所有方法会返回一个plt.text对象
import numpy as np
import matplotlib.pyplot as plt
import math

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)
t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.cos(2*np.pi*t)
ax1.plot(t, s1)
ax2.plot(t, s2)

# # 设置标题
# ax1.set_title(r'sin$\alpha_i$',fontsize=20)  # 书写数学符号得前加r去掉转义字符，中间加$
#
# # 任意位置添加内容
# # ax1.text(0.05,0.95,r'$\mathcal{A}\mathrm{sin}(2 \omega t)$',transform=ax1.transAxes,style='italic',bbox=dict(boxstyle='round,pad=0.5',facecolor='red',edgecolor='black'))
#
# # 添加图例
# ax1.legend(labels='s',loc = 'upper right')
#
# ax2.set_title(r'cos$\alpha_i$',fontsize=20)
#
# # 设置中心标题
# plt.suptitle('test',fontsize=20)
#
# # 在figure对象任意位置添加内容
# plt.figtext(.5,.5,r'$\alpha_i$',fontsize=20)

# 设置注释
ax1.annotate('sinx', xy=(1.5, 0.8), xytext=(1, 0.4), arrowprops=dict(facecolor='black', shrink=0.01))
plt.show()
