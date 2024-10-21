print("#패킹과 언패킹=========================")

"""
z01 = 10
z02 = 20
z03 = "python"

t = [z01, z02, z03]
print(t)
"""

t = 10, 20, "python"  # 튜플로 묶어서 변수에 할당  *읽기전용 리스트5
print(t)
print(type(t))

# t[2]= "java"  #튜플이라서 값을 바꿀수 없다

print(t)
print(t[0], t[1], t[2])

"""
item01 = t[0]
item02 = t[1]
item03 = t[2]
print(item01)
print(item02)
print(item03)
"""
item01, item02, item03 = t

print(item01)
print(item02)
print(item03)
