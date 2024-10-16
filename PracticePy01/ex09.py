# [문제] Ex18 사용자로부터 화씨 온도를 입력받아 섭씨 온도로 변환하는 프로그램을 작성하세요.

fahrenheit = float(input("화씨 온도를 입력하세요: "))

# 섭씨로 변환하는 공식
celsius = 5 / 9 * (fahrenheit - 32)

print(f"섭씨 온도는 {celsius} 입니다.")
