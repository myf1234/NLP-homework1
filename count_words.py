from collections import Counter
import jieba
import csv

file_name = 'preprocessed_text.txt'  # 你的文件名

with open(file_name, 'r', encoding='utf-8') as file:
    text = file.read()  # 读取文件内容到变量text

# 建表
words_list = text.split()

word_counts = Counter(words_list)
  
# 使用 sorted() 对字典进行排序，key 指定排序依据为字典的值（频率），reverse=True 表示降序排序
sorted_word = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

# 指定CSV文件名
csv_file_path = 'word_frequencies.csv'

# 打开文件进行写入csv
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
    # 创建csv写入器
    writer = csv.writer(csvfile)
    # 写入标题行
    writer.writerow(['Word', 'Frequency'])
    # 遍历词频数据，并写入
    for word, freq in sorted_word:
        writer.writerow([word, freq])

print(f"词频数据已保存到 {csv_file_path}")
