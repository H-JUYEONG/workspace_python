PI = 3.14


# 더하기 함수
def plus(a, b):
    return a + b


# 빼기 함수
def minus(a, b):
    return a - b


# 곱하기 함수
def multi(a, b):
    return a * b


# 나누기 함수
def div(a, b):
    return a / b


# 원의 넓이
def area_circle(r):
    return PI * r**2


# 이파일을 실행일때만 실행됨
if __name__ == "__main__":
    print("=============================")
    print(plus(55, 66))
    print(area_circle(5))
