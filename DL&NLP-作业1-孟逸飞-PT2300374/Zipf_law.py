import pandas as pd
import matplotlib.pyplot as plt

# CSV 文件的路径
csv_file_path = 'word_frequencies.csv'

# 读取 CSV 文件
df = pd.read_csv(csv_file_path)

# 获取词频列，假设列名为 'Frequency'
frequencies = df['Frequency'].tolist()

# 生成排名列表
ranks = list(range(1, len(frequencies) + 1))

plt.figure(figsize=(10, 6))
plt.loglog(ranks, frequencies, marker=".", linestyle='None', markersize=12)
plt.title('Zipf\'s Law')
plt.xlabel('Rank')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
