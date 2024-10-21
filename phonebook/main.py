import phonebookdao as dao

print("********************************************")
print("*          전화번호 관리 프로그램          *")
print("********************************************")
print("")

while True:
    print("1.리스트  2.등록  3.삭제  4.검색  5.종료")
    print("--------------------------------------------")
    num = int(input(">메뉴번호: "))

    if num == 1:
        print("<1.리스트>")
        dao.get_person_list()

    elif num == 2:
        print("<2.등록>")
        name = input(">이름: ")
        hp = input(">휴대전화: ")
        company = input(">회사전화: ")
        dao.add_person(name, hp, company)

    elif num == 3:
        print("<3.삭제>")
        del_num = int(input(">번호: "))
        dao.del_person(del_num)

    elif num == 4:
        print("<4.검색>")
        keyword = input("이름: ")
        dao.get_keyword_list(keyword)

    elif num == 5:
        print("")
        print("********************************************")
        print("*                감사합니다                 *")
        print("********************************************")
        print("")
        break
    else:
        print("[다시 입력해 주세요.]")
