str1 = "FirstString"
str2 = "SecondString"
print(str1 + str2)

print(str1 * 3)

print("=" * 50)
print("My program")
print("=" * 50)

s = "First String"
print(s[0], s[1], s[4])
print(s[0] + s[1] + s[4])

# 같은표현 마지막글자
print(s[11])
print(s[-1])

# 같은표현 첫번째글자
print(s[0])
print(s[-12])

# [0], [-0]
print(s[0], s[-0])

# 예제 F r _ S g
print(s[0], s[2], s[5], s[6], s[11])
print(s[-12], s[-10], s[-7], s[-6], s[-1])

print("===========================================")
print(s[0] + s[1] + s[2] + s[3] + s[4])
print(s[0:5])  # 이상  5미만   0번부터 4번까지
print(s[:5])  # 0은 생략할수 있다

print("===========================================")
print(s[1:9:3])  # 1부터 8번까지 3씩 증가
print(s[3:])  # 3부터 끝까지
print(s[:])  # 처음부터 끝까지
print(s[-6:-2])

print(s[::-1])  # 문자열을 역으로 출력한다

# s[5] = "a"
print(s)
s = "FirstaString"

name = "토마토"
name2 = name[::-1]

print(name)
print(name2)

print(name == name[::-1])
