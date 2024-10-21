# 0.import
import mysql.connector
from mysql.connector import Error


host = "localhost"  # 호스트
user = "phonebook"  # 사용자명
password = "phonebook"  # 비밀번호
database = "phonebook_db"  # 데이터베이스명


# connect() 함수
def get_connect():
    conn = mysql.connector.connect(
        host=host,  # 호스트
        user=user,  # 사용자명
        password=password,  # 비밀번호
        database=database,  # 데이터베이스명
    )
    return conn


# close 함수
def close(conn, cursor):
    if cursor is not None:
        cursor.close()
    if conn is not None:
        conn.close()


# insert
def add_person(name, hp, company):

    try:
        # 1.연결/컨넥션 얻기
        conn = get_connect()

        # 2.커서생성
        cursor = conn.cursor()

        # 3.SQL문준비  / 바인딩 / 실행
        # --SQL문
        query = """
            insert into person
            values(null, %s, %s, %s)
        """
        # --바인딩(튜플)
        data = (name, hp, company)

        # --실행
        cursor.execute(query, data)  # 실행(임시)
        conn.commit()  # 반영(실제)  리턴값은 없다

        # 4.결과처리
        print(f"{cursor.rowcount}건 등록되었습니다.")

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        # 5.자원정리
        close(conn, cursor)


# select
def get_person_list():
    try:
        # 1.연결/컨넥션 얻기
        conn = get_connect()

        # 2.커서생성
        cursor = conn.cursor()

        # 3.SQL문준비  / 바인딩 / 실행
        # --SQL문
        query = """
            select person_id,
                name,
                hp,
                company
            from person
        """

        # --바인딩(튜플)

        # --실행
        cursor.execute(query)
        resultset = cursor.fetchall()

        # 4.결과처리    리스트[(튜플), (튜플), (튜플)] --> 리스트[(딕션어리), (딕션어리), (딕션어리)]
        # print(resultset[0][1])
        person_list = []
        for row in resultset:
            person_vo = {
                "person_id": row[0],  # person_id
                "name": row[1],  # name
                "hp": row[2],  # hp
                "company": row[3],  # company
            }
            person_list.append(person_vo)

        for list in person_list:
            print(list)

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        # 5.자원정리
        close(conn, cursor)


# delete
def del_person(del_num):

    try:
        # 1.연결/컨넥션 얻기
        conn = get_connect()

        # 2.커서생성
        cursor = conn.cursor()

        # 3.SQL문준비  / 바인딩 / 실행
        # --SQL문
        query = """
            delete from person
            where person_id = %s
        """
        # --바인딩(튜플)
        data = (del_num,)

        # --실행
        cursor.execute(query, data)  # 실행(임시)
        conn.commit()  # 반영(실제)  리턴값은 없다

        # 4.결과처리
        print(f"{cursor.rowcount}건 삭제되었습니다.")

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        # 5.자원정리
        close(conn, cursor)


# keyword
def get_keyword_list(keyword):
    try:
        # 1. 연결/컨넥션 얻기
        conn = get_connect()

        # 2. 커서 생성
        cursor = conn.cursor()

        # 3. SQL문 준비 / 바인딩 / 실행
        query = """
            select person_id,
                   name,
                   hp,
                   company
            from person
            where name like %s
        """

        # -- 바인딩할 파라미터 설정 (키워드를 포함한 와일드카드)
        data = (f"%{keyword}%",)  # 튜플로 만듦

        # -- 실행
        cursor.execute(query, data)  # 쿼리와 함께 파라미터 전달
        resultset = cursor.fetchall()

        # 4. 결과 처리
        person_list = []
        for row in resultset:
            person_vo = {
                "person_id": row[0],  # person_id
                "name": row[1],  # name
                "hp": row[2],  # hp
                "company": row[3],  # company
            }
            person_list.append(person_vo)

        # 결과 출력
        for person in person_list:
            print(person)

    except Error as e:
        print(f"데이터베이스 오류: {e}")

    finally:
        # 5. 자원 정리
        close(conn, cursor)
