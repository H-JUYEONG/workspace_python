# 총급액을 입력하면 백원단위는 할인을 해주고 있습니다. 실제 지불금액을 출력하는 코드를 작성하세요

total_amount = int(input("전체 금액을 입력해주세요: "))

payable_amount = (total_amount // 100) * 100

print(f"실제 지불 금액은 {payable_amount}원 입니다.")