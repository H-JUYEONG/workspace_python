# 대입문
a = 3
b = 5
c = a + b
print(a, b, c)

# 대입문 오류
# 1+3 = a

# 한줄에 표기할때는 ; 로 구분
e = 3.5
f = 5.3
print(e, f)

# 여러 변수를 한번에 대입
g, h, i = 3.5, 5.3, 100
"""
g=3.5
h=5.3
i=100
"""
print(g, h, i)

# 여러 개를 같은 값 10으로 대입
x = y = z = 10
"""
x=10
y=10
z=10
"""
print(x, y, z)


# 값 교환하기 다른 언어에서는  임시변수를 만들어야함
j = 3.5
k = 100

j, k = k, j
print(j, k)

"""
temp = j
j = 100
k = temp
print(j, k)
"""

# 같은이름의 변수 사용가능
num = 1
print(type(num), num)

num = "hello"
print(type(num), num)
