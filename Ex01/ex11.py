s = "i like Python"

print(s.upper())  # 대문자로 변환
print(s.lower())  # 소문자로 변환
print(s.swapcase())  # 소문자로 변환
print(s.capitalize())  # 소문자로 변환
print(s.title())  # 단어의 첫번재만 대문자로 변환
print(s)  # 원본은 변하지 않는다

print("===========================================")
s = "I Like Python. I Like Java Also"
print(s.count("Like"))  # 2:  'Like' 가 몇개?


print(s.find("Like"))  # 2:  첫번째 'Like' 의 시작 "index번호"
print(s.find("Like", 5))  # 17:  index번호가 5 이후에 처음 나타나는 'Like' index번호
print(s.find("JS"))  # -1: 첫번째 'JS' 의 시작 index번호  없으면 -1
print(s.rfind("a"))  # 25:  오른쪽부터 첫번째 'a'의 index번호
# print(s.lfind('a'))         #    lfind() 함수는 없음 주의

print("============================")
print(s.index("Like"))  # 2 : 첫번째 'Like' 의 시작 index번호
# print(s.index('JS'))       #에러 : 첫번째 'JS' 의 시작 index번호,없으면 에러남
# print(s.rindex('Like'))     #17 : 오른쪽부터 첫번째 'like'의 index번호,없으면 에러남

print(s.startswith("I Like"))  # true : 'I Like' 로 시작하면 true  아니면 false
print(
    s.startswith("Like", 2)
)  # true : 'Like' 가 index번호 2번에서 시작하면 true  아니면 false
print(s.endswith("Also"))  # true : 'Also' 로 끝나면 true 아니면 false
print(
    s.endswith("Java", 0, 24)
)  # false : index번호가 0부터 24번 사이에 'Java' 로 끝나면 true 아니면 false

print("============================")
s = "    spam and ham    "
print("|" + s + "|")
print("|" + s.strip() + "|")
print("|" + s.lstrip() + "|")
print("|" + s.rstrip() + "|")

s = "<><abc><><defg><><>"
print(s.strip("<"))
print(s.strip(">"))

print(s.strip("<>"))  # 체크  <abc><><defg><> X, <abc><><defg> X
print(s.strip("<>a"))

# 치환
s = "Hello Java Java java"
print(s.replace("Java", "Python"))  # Hello Python Python java   #Java ---> Python

# 정렬
s = "king and queen"
print("|" + s.center(60) + "|")  # 60칸에서 가운데
print(s.center(60, "-"))  # 60칸에서 가운데 공백은 '-'기로로 채우기
print(s.ljust(60, "-"))  # 60칸에서 왼쪽 공백은 '-'기호로 채우기
print(s.rjust(60, "#"))  # 60칸에서 오른쪽 공백은 '#'기호로 채우기


# 판별
s01 = "1234"
s02 = "abcd"
s03 = "ABCD"

print(s01.isdigit())  # True:  문자열이 숫자이면 True 아니면 Falss
print(s02.isdigit())  # False:  문자열이 숫자이면 True 아니면 Falss

print(s01.isalpha())  # False:  문자열이 알파벳이면 True 아니면 Falss, 한글?
print(s02.isalpha())  # True:  문자열이 알파벳이면 True 아니면 Falss, 한글?

print(s02.islower())  # True:  문자열이 소문자이면 True 아니면 Falss
print(s03.isupper())  # True:  문자열이 소문자이면 True 아니면 Falss


print("============================")
print("\n\n".isspace())  # True:  문자열이 공백이면 True 아니면 Falss
print("    ".isspace())  # True:  문자열이 공백이면 True 아니면 Falss
print("".isspace())  # False:  문자열이 공백이면 True 아니면 Falss
print(" a  ".isspace())  # False:  문자열이 공백이면 True 아니면 Falss

print("25".zfill(10))  # 0000000025
print("1234".zfill(10))  # 0000001234
print("12345678912345".zfill(10))  # 1234567891234
print("  abcd".zfill(10))  # 0000__1234
print("13".zfill(2) + ":" + "7".zfill(2))  # 사용예시 03시07분
