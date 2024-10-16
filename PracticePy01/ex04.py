# 직사각형의 둘레와 면적을 구하는 프로그램을 작성하세요.(가로 세로 변수 double형으로 작성)

width = int(input("가로를 입력하세요: "))
height = int(input("세로를 입력하세요: "))

print(f"사각형의 넓이는 {float(width * height)}")
print(f"사각형의 둘레는 {float(2 * (width + height))}")
