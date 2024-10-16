# 사용자에게 연필의 개수와 인원수를 입력받아 모든인원에게 같은수의 연필을 나눠주려고 한다
# 1인당 연필의 받을수 있는 연필의 개수와 나머지를 구하시오

pencil = int(input("전체 연필갯수를 입력해주세요: "))
people = int(input("전체 인원수를 입력해주세요: "))

pencils_per_person = pencil // people  # 정수 몫만 필요할 때 // 사용
remaining_pencils = pencil % people

# 결과 출력
print(f"1인당 연필의 갯수는 {pencils_per_person} 입니다.")
print(f"연필의 나머지 갯수는 {remaining_pencils} 입니다.")
