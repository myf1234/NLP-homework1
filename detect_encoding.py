import chardet

def detect_encoding(file_path):
    with open(file_path, 'rb') as file:  # 以二进制模式读取文件内容
        raw_data = file.read()
    encoding = chardet.detect(raw_data)['encoding']
    return encoding

file_path = 'jyxstxtqj_downcc.com\三十三剑客图.txt'
encoding = detect_encoding(file_path)
print(f"Detected encoding: {encoding}")