# 정수형
a = 101
print(a, type(a))
print(isinstance(a, int))

# 2진수 8진수 16진수 -> 10진수로 표현
b = 0b10
print(b)

c = 0o10
print(c)

d = 0x1A
print(d)

# 10진수로 표현 -> 2진수 8진수 16진수
print(bin(5))
print(oct(65))
print(hex(257))


# 큰수(지수)
e = 2**1024
print(e, type(e))
