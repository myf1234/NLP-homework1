import jieba
import re
from collections import Counter

# 读取停用词内容的函数
def load_stopwords(path):
    with open(path, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

# 读取语料库内容并整合在一起的函数
def read_text(file_paths):
    all_text = ""
    for file_path in file_paths:
        with open(file_path, 'r', encoding='GB2312',errors='replace') as file:
            all_text += file.read() + "\n"  # 加一个换行符，以便分隔不同文件的内容
    return all_text

# 整理语料库内容的函数
def clean_text(text):
    # 使用正则表达式替换掉所有英文字符（大写和小写）、数字和特殊符号
    cleaned_text = re.sub(r'[a-zA-Z0-9\u3000\n]', '', text)
    return cleaned_text

# 对语料库内容进行分词的函数
def preprocess_chinese_text(text, stopwords):
    # 使用 jieba 进行分词
    words = jieba.cut(text)
    # 去除停用词和标点符号
    cleaned_text = ' '.join(word for word in words if word not in stopwords)
    return cleaned_text

# 分词结束后到处内容的函数
def write_text_to_file(text, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


# 停用词文件路径为 'cn_stopwords.txt'
stopwords = load_stopwords('cn_stopwords.txt')

# 语料库文件路径
file_paths = ['jyxstxtqj_downcc.com\三十三剑客图.txt',
'jyxstxtqj_downcc.com\书剑恩仇录.txt',
'jyxstxtqj_downcc.com\侠客行.txt',
'jyxstxtqj_downcc.com\倚天屠龙记.txt',
'jyxstxtqj_downcc.com\天龙八部.txt',
'jyxstxtqj_downcc.com\射雕英雄传.txt',
'jyxstxtqj_downcc.com\白马啸西风.txt',
'jyxstxtqj_downcc.com\碧血剑.txt',
'jyxstxtqj_downcc.com\神雕侠侣.txt',
'jyxstxtqj_downcc.com\笑傲江湖.txt',
'jyxstxtqj_downcc.com\越女剑.txt',
'jyxstxtqj_downcc.com\连城诀.txt',
'jyxstxtqj_downcc.com\雪山飞狐.txt',
'jyxstxtqj_downcc.com\飞狐外传.txt',
'jyxstxtqj_downcc.com\鸳鸯刀.txt',
'jyxstxtqj_downcc.com\鹿鼎记.txt']

# 读取并合并这些文件的内容
text = read_text(file_paths)

# 应用函数去除字母等
text_new = clean_text(text)

# 使用之前定义的预处理函数和步骤来处理这个合并后的文本
preprocessed_text = preprocess_chinese_text(text_new, stopwords)


# 指定输出文件的路径
output_path = 'preprocessed_text.txt'

# 将预处理后的文本写入到文件中
write_text_to_file(preprocessed_text, output_path)

print(f"预处理后的文本已保存到 {output_path}")



