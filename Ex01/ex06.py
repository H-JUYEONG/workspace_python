# 복소수
a = 4 + 5j
print(a)
print(type(a))
print(isinstance(a, complex))

b = 4 + 5j
c = 7 - 2j
print(b + c)
print(type(b + c))
print(b.real, b.imag)


# 정수 --> 복소수
d = 5
print(d, type(d))
print(complex(d), type(complex(d)))

# 실수 --> 복소수
e = 7.5
print(e)
print(complex(e))


# 정수 --> 실수
print(float(d))

# 실수 --> 정수
print(int(e))
