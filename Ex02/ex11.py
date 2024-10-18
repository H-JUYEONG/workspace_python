x = 5  # global 글로벌


def calPlus(no):
    return no + x


print(calPlus(10))  # 10 + 5

print("-------------------------------")


def calPlus2(no):  # local 로컬
    x = 1
    return no + x


print(calPlus2(10))  # 10 + 1

print("-------------------------------")


# 블록 스코프
def calPlus3(mode, no):  # local 로컬
    if mode == 1:
        sum = no + 1
    elif mode == 2:
        sum = no + 2
    else:
        print("에러")
    return sum


g = 1


def func3(a):
    global g
    g = 3
    return a + g


print(func3(10))
print(g)
