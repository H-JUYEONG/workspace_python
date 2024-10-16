num = input("숫자를 입력하세요")
print(type(num))
num = int(num)

if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("0입니다.")


num = int(input("숫자를 입력하세요"))
print(type(num))

if num % 2 == 0:
    print("짝수")
elif num < 0:
    print("음수")
else:
    print("홀수")


code = int(input("과목번호를 입력해 주세요\n"))
match code:
    case 1:
        print("R101호")
    case 2:
        print("R202호")
    case 3:
        print("R303호")
    case 4:
        print("R404호")
    case _:
        print("상담원에게 문의하세요")
