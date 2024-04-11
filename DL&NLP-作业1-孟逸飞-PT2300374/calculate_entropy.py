import numpy as np

# 文件路径
file_path = 'preprocessed_text.txt'

# 读取文件内容
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# 以词为单位计算信息熵
def calculate_entropy_word(text):
    words = text.split()  # 词之间通过空格分隔
    word_counts = {}
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    total_words = sum(word_counts.values())
    word_probs = [count / total_words for count in word_counts.values()]
    entropy = -np.sum([p * np.log2(p) for p in word_probs])
    return entropy

# 以字为单位计算信息熵
def calculate_entropy_char(text):
    char_counts = {}
    for char in text.replace(" ", ""):  # 去除空格，只计算字符
        char_counts[char] = char_counts.get(char, 0) + 1
    total_chars = sum(char_counts.values())
    char_probs = [count / total_chars for count in char_counts.values()]
    entropy = -np.sum([p * np.log2(p) for p in char_probs])
    return entropy

# 计算并打印结果
entropy_word = calculate_entropy_word(text)
entropy_char = calculate_entropy_char(text)
print(f"以词为单位的信息熵: {entropy_word}")
print(f"以字为单位的信息熵: {entropy_char}")
