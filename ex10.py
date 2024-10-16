# 빛이 1년동안 진행하는 거리를 계산하여 출력하세요.
# (단 빛의 속도는 300000 km/s 로 계산한다)

# 빛의 속도 (km/s)
speed_of_light = 300000  # 300,000 km/s

# 초당 거리 계산 (1년 = 365일 * 24시간 * 60분 * 60초)
seconds_per_year = 365 * 24 * 60 * 60

# 빛이 1년 동안 가는 거리
distance_in_one_year = speed_of_light * seconds_per_year

# 결과 출력
print(f"빛이 1년 동안 가는 거리는 {distance_in_one_year} km 입니다.")
