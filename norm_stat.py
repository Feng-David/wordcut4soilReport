import matplotlib.pyplot as plt
from jieba_1 import word_counts




# 绘制词频统计曲线
plt.plot(word_counts.values, alpha=0.6, color='blue')

plt.ylabel('Frequency Count', fontsize=15)
plt.title('Token Frequency Count', fontsize=20)

plt.show()
