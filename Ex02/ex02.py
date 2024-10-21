print("=튜플 기본===============================================")

t = (1, 2, 3, 4)  # 리스트--> a = [1,2,3,4]
print(type(t))  # <class 'tuple'>

# 수정불가, 읽기는 가능
print(t[0], t[1], t[2])  #  + index
print(t[-1], t[-3])  #  - index

print(t[1:3])  # (2, 3)  --> 튜플
print(t[:])  # 튜플

print(t * 2)  # 원본은 수정되지 않음 (수정의 개념이 아님)
print(t)

print(t + (100, 200, 300))  # 원본은 수정되지 않음 (수정의 개념이 아님)
print(t)

print(len(t))
print(3 in t)  # 튜플에 3이 있냐? True False로 리턴


print("=튜플 생성===============================================")
t = (1, 2, 3, 4)  # 리스트--> a = [1,2,3,4]

tt = 100, 200, 300
print(tt)

t = 99  # 값이 하나만 있을때는 숫자다
t = (99,)  # 값이 한개일때 튜플 생성방법
print(t)

print("=튜플 값 변경(X)=========================================")
t = ("apple", "banana", 10, 20)
# t[0] = "mango"
# t[2] = 100
print(t[2] + 10)

# t[1:2] = (1000, 2000)


a_list = list(t)
print(type(t))
print(type(a_list))

t = ("apple", "banana", 10, 20)
for item in t:
    print(item)

print("--------------------")
for index, item in enumerate(t):
    print(item)
