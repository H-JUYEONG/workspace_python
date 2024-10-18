print("********************************************")
print("*          전화번호 관리 프로그램          *")
print("********************************************")
print("")

file_path = "C:\\javaStudy\\workspace_python\\Ex02\\PhoneDB.txt"

while True:
    print("1.리스트  2.등록  3.삭제  4.검색  5.종료")
    print("--------------------------------------------")
    num = int(input(">메뉴번호: "))

    if num == 1:

        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()  # 전체 내용 읽기
            print(content)
    elif num == 2:
        with open(file_path, "w", encoding="utf-8") as file:
            file.write("학교종이 땡땡땡\n")
