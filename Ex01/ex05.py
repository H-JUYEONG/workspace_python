# 실수형

a = 1.2
print(type(a))
print(isinstance(a, float))
print(a.is_integer())


# 100000 = 105 = 1.0*105 = 1.0*e+5  -> 1.0e5
b = 1.0e5  # b = 1.0E5
print(b)

# 0.01 = 10-2 = 1.0*10-2 = 1.0*e-2  -> 1.0e-2
c = 1.0e-2  # c = 1.0E-2
print(c)


d = 3e3  # 3.0*10의 3승
print(d)

e = -0.2e-4
print(e)
