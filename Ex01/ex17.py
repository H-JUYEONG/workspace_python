num = input("숫자를 입력하세요\n")
int_num = int(num)

if int_num > 0:
    print("양수")
elif int_num < 0:
    print("음수")
else:
    print("0입니다.")
