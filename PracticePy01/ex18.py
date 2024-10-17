# 1~45까지의 숫자 중 임의의 6개의 숫자를 출력하세요-미니로또
# 랜덤함수 검색해볼것
# 중복체크 할 것

import random

# 1부터 45까지의 숫자 중에서 6개의 임의의 숫자 추출
lotto_numbers = random.sample(range(1, 100), 6)

# 출력된 숫자를 오름차순으로 정렬 (선택 사항)
lotto_numbers.sort()

# 결과 출력
print("로또 번호:", lotto_numbers)
