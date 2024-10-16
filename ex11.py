# 동전별 개수를 입력받아 총금액을 계산하는 프로그램을 작성하세요.

coin500 = int(input("500원 개수: "))
coin100 = int(input("100원 개수: "))
coin50 = int(input("50원 개수: "))
coin10 = int(input("10원 개수: "))

total500 = coin500 * 500
total100 = coin100 * 100
total50 = coin50 * 50
total10 = coin10 * 10

total = total500 + total100 + total50 + total10
print(f"동전의 총합은 {total} 원 입니다.")
