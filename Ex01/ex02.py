#  대입문

a = 3
b = 5
c = a + b
print(a, b, c)

# 대입문
e = 3.5
f = 5.3
print(e, f)

# 여러변수를 한번에 대입
g, h, i = 1.2, 335, 8.7
print(g, h, i)

# 여러개를 같은 값으로 대입
y = z = 10
print(y, z)
"""
x=10
y=10
z=10
"""

# 값 교환하기 : 다른 언어에서는 임시변수를 만들어줘야했음
j = 3.5
k = 100

j, k = k, j
print(j, k)

""" 이제까지 방식
temp = 3.5
j = k
k = temp
print(j,k)
"""

# 같은 이름의 변수 사용가능
num = 1
print(type(num), num)

num = "hello"
print(type(num), num)
