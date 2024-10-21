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
        print("상담원")
