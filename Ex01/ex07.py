# 수치 연산자

# 산술 연산자
print(8 * 3)  # 24
print(8 + 3)  # 11
print(8 - 3)  # 5
print(8 / 3)  # 2.6666666666666665

print(8 / 3)  # 2.6666666666666665
print(8.0 / 3)  # 2.6666666666666665
print(8 / 3.0)  # 2.6666666666666665
print(8.0 / 3.0)  # 2.6666666666666665

print(9 / 3)  # 3.0
print(9 / 3.0)  # 3.0

print("---------------------------------------")
print(10 / 3)  #
print(10 // 3)  # 3     몫 연산자
print(10 % 3)  # 1     나머지 연산자
print(divmod(10, 3))  # (3,1) 몫 과 나머지를 구하는 함수
print(8**2)

print("---------------------------------------")

# 연산자 우선순위
print(2 + 3 * 4)  # 14
print(-2 + 3 * 4)  # 10
print(-(2 + 3) * 4)  # -20
print((-2 + 3) * 4)  # 4
print(4 / 2 * 2)  # 4.0
print(4 / (2 * 2))  # 1.0

print((2**3) ** 4)  # 8*8*8*8

print(2 ** (3**4))  # 2 ** 81
print(2**3**4)


x, y = divmod(10, 3)
print(x)
print(y)
