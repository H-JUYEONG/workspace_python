# 확장연산자

x = 3
# x = x + 3
x += 3
print(x)

y = 10
# y = y**2
y **= 2
print(y)

print("================================")
# 관계 연산자
print(1 > 3)  # False
print(2 < 4)  # True
print(4 <= 5)  # True
print(4 >= 5)  # False
print(6 == 9)  # False
print(6 != 9)  # True


a = 6
print(0 < a < 10)
print(0 < a and a < 10)

print("================================")

a = 10
b = 20
c = a
d = 11
e = 11

print(id(a))  # 10
print(id(b))  # 20
print(id(c))  # 10
print(id(d))  # 11
print(id(e))  # 11

# 값비교 == ,  is
print(a == b)  # 값비교
print(a is b)  # 주소비교
print(a is c)  # 주소비교
print(a is d)  # 주소비교
print(d is e)  # 주소비교


print("================================")
# 논리연산자
print(True and True)
print(False and True)

print(False or True)

print(not (False or True))

print("================================")
print(abs(-3))  # 절대값  -> 3
print(abs(3))  # 절대값  -> 3

print(int(3.1415))  # 정수형으로(실수)  -> 정수
# print(int(3+4j))     # 정수형으로(복소수) -> 오류
print(int("4"))  # 정수형으로(문자열) -> 정수
# print(int("5.45"))    # 정수형으로(문자열) -> 오류

print(float(3))  # 실수형으로(정수) -> 실수
print(float("4"))  # 실수형으로(문자열) -> 실수
# print(float(4+5j))        # 실수형으로(복소수) -> 오류

print(complex(3))  # 복소수형으로(정수) -> 복소수
print(complex("3"))  # 복소수형으로("문자열") -> 복소수
print(complex("3+5j"))  # 복소수형으로("문자열") -> 복소수

print(pow(2, 10))  # 2**10
