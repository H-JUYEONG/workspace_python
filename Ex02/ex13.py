file_path = "C:\\javaStudy\\workspace_python\\Ex02\\PhoneDB.txt"

file = open(file_path, "r", encoding="utf-8")
data = file.read()
print(data)

file.close()


# 파일 한줄씩 읽기
file = open(file_path, "r", encoding="utf-8")

for line in file:
    print(line.strip())

file.close()


with open(file_path, "r", encoding="utf-8") as file:
    content = file.read()  # 전체 내용 읽기
    print(content)
