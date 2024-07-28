# 箱形图也称为须状图，显示包含最小值，第一四分位数，中位数，第三四分位数和最大值的一组数据的摘要
# ax.boxplot(
import numpy as np
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
np.random.seed(10)
collection_1 = np.random.normal(100,10,200)  # 高斯分布
collection_2 = np.random.normal(80,30,200)
collection_3 = np.random.normal(90,20,200)
collection_4 = np.random.normal(70,25,200)

ax.boxplot([collection_1,collection_2,collection_3,collection_4])
ax.set_title('gs fenbu')
ax.set_xticklabels(['collection_1','collection_2','collection_3','collection_4'])
plt.show()
