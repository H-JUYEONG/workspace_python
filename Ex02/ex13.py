file_path = "C:\\javaStudy\\workspace_python\\Ex02\\PhoneDB.txt"

# 파일 한번에 읽기
file = open(file_path, "r", encoding="UTF-8")
data = file.read()
print(data)
file.close()

# 파일 한번에 읽기(2) : close를 생략하게 해준다. 자동으로 해줌.
print("-----파일 한번에 읽기(2)-----")
with open(file_path, "r", encoding="UTF-8") as file:
    data = file.read()
    print(data)


# 파일 한 줄씩 읽기
print("-----파일 한줄씩 읽기-----")
file = open(file_path, "r", encoding="UTF-8")
for line in file:
    print(line.strip())  # 줄바꿈, 공백, 탭, 삭제(문자열이 갖고 있는 메소드)
file.close()


# 파일 한 줄씩 읽기(2)
print("-----파일 한줄씩 읽기(2)-----")
with open(file_path, "r", encoding="UTF-8") as file:
    for line in file:
        print(line.strip())
