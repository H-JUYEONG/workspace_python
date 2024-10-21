s = ""  # '' 를 사용해도 된다
str1 = "hello world"
str2 = "안녕세상"

print(s, str1, str2)
print(type(s), type(str1), type(str2))
print(isinstance(str2, str))

# 나는 "정우성" 입니다.
str3 = '나는 "정우성" 입니다.'
# str3 = "나는 \"정우성\" 입니다."
print(str3)

# 나는 '박명수' 입니다.
# str4 = "나는 '박명수' 입니다."
str4 = "나는 '박명수' 입니다."
print(str4)

print("====================================")
s01 = "aaa"
s02 = "aaa"
print(s01, id(s01))
print(s02, id(s02))

s02 = "bbbb"
print(s01, id(s01))
print(s02, id(s02))

print("====================================")

str5 = """ABCDEFG 
'abc'def 
"가나다"라마바사 
1234567899"""
print(str5)

print("====================================")

# Hello World I'd say "hello World"
print('Hello World I\'d say "hello World"')  # ""를 기본으로 사용
print('Hello World I\'d say "hello World"')  #''를 기본으로 사용

print('Hello\nWorld I\'d say "hello World"')

print("hello!!!!!!!!\rworld")  # 커서가 현재줄의 맨앞으로 간다
print("hello\b\b\bworld")  # 한칸씩 앞으로 간다

print("hello\tw\torld")
