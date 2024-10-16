# 값,주소 비교
a = 10
b = 20
c = a
d = 11
e = 11

# 주소값 출력하는 함수 id()
# 같는 값은 같은 주소
print(id(a))  # 10-->140735392631512
print(id(b))  # 20-->140735392631832
print(id(c))  # 10-->140735392631512  a와 같은 주소
print(id(d))  # 11-->140735392631544
print(id(e))  # 11-->140735392631544  d와 같은 주소

# == 값비교   is() 주소값비교
print(a == b)  # False
print(a is b)  # False
print(a is c)  # True
print(a is d)  # False
print(d is e)  # True
