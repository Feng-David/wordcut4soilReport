import jieba
import os
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
# 加载停用词列表
stopwords = set()
with open('stopwords.txt', 'r', encoding='utf-8') as f:
    for word in f:
        stopwords.add(word.strip())

# 合并多个文件的分词结果
all_tokens = []
for filename in os.listdir('txt_files'):
    with open(os.path.join('txt_files', filename), 'r', encoding='utf-8') as f:
        text = f.read()
        tokens = jieba.lcut(text)
        tokens = [token for token in tokens if token not in stopwords]
        all_tokens.extend(tokens)

# 将分词结果写入文件
with open('segmented_text.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(all_tokens))
# 读取分词结果
with open('segmented_text.txt', 'r', encoding='utf-8') as f:
    tokens = f.read().split()

# 创建DataFrame
df = pd.DataFrame({'分词': tokens})

# 导出DataFrame为txt文件
df.to_csv('tokens.txt', index=False, header=False, sep='\t', encoding='utf-8')

# 计算词频
word_counts = df['分词'].value_counts()



# 绘制词频统计图
# 只统计前100个分词
top_100 = word_counts[:100].sort_values(ascending=True)
t100=top_100/word_counts.sum()
t100.plot(kind='barh', figsize=(50, 75), fontsize=35)

plt.xlabel('词频', fontsize=15)
plt.ylabel('分词', fontsize=15)
plt.title('词频统计', fontsize=20)

# 保存词频统计图
plt.savefig('word_frequency_count.png', bbox_inches='tight')

# 导出前100个词频
top_100.to_csv('top_100_tokens.txt', header=False, index=True)

plt.show()
