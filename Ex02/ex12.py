num = int(input("숫자를 입력하세요\n"))

try:
    result = 100 / num
    print(result)
except FileNotFoundError as e:
    print(e)

finally:
    print("공통영역")


print("프로그램 정상종료")
