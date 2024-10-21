# bool형
a = 1
b = a > 10
print(b, type(b))


# bool형 연산
# True -> 1,  False -> 0
print(True + True)  # 1 + 1
print(1 == True)  # 1 == 1
print(0 == False)  # 0 == 0

# bool형과 정수형 연산
b1 = True
b2 = False
print(b1 + 10)  # True+10 -> 1+10 -> 11
print(b2 + 10)  # True+10 -> 0+10 -> 10
