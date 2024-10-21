"""
java
public int plus(a, b){
    sum = a+b;
    return sum;
}

js
function plus(a,b){
    sum = a+b;
    return sum;
}

let plus = function(){
    sum = a+b;
    return sum;
}

let plus = ()=>{
    sum = a+b;
    return sum;
}
"""


# 정의
def plus(a, b):
    sum = a + b
    return sum


# 실행
result = plus(5, 3)
print(result)

"""
result = plus(5,"한글")  #숫자+문자열X
print(result)
"""
print("===========================")


# 정의
def my_function():
    print("hello function")


# 실행
my_function()

print("===========================")


# 정의
def none_function():
    pass


# 사용
none_function()

print(type(none_function))


print("===========================")
result = 8, 15
print(result)


# 정의
def sum_and_mul(a, b):
    sum = a + b
    mul = a * b
    return sum, mul  # 패킹(튜플)


# 언패킹 사용안할때
result = sum_and_mul(5, 3)
sum = result[0]
mul = result[1]
print(sum)
print(mul)

# 언패킹 사용
sum, mul = sum_and_mul(5, 3)
print(sum)
print(mul)

print("===========================")


# 정의
def plus_print(a=0, b=999):
    print(f"{a} + {b} = {a+b}")


plus_print(3, 5)  # a=3  b=5    #파라미터를 위치로 매칭
plus_print(3)  # a=3  b=0
plus_print()  # a=0  b=0

print("------------------------")
# plus_print(,333)  # 오류
plus_print(b=333)  # 파라미터를 이름으로 매칭
plus_print(b=333, a=2)  # 파라미터를 이름으로 매칭


print("------------------------")
"""
sum_many(1,2)
sum_many(1,2,3)
sum_many(1,2,3,4,5,6,7,8)
"""


# 정의
def sum_many(*args):
    sum = 0
    for no in args:
        # sum = sum + no
        sum += no
    print(sum)
    print("-------------")


sum_many(1, 2)
sum_many(1, 2, 3)
sum_many(1, 2, 3, 4, 5, 6, 7, 8)


print("=======================================")
"""
sum_mul("sum", 1,23,45)
sum_mul("mul", 1,23,45,22,2333)
"""


# 정의
def sum_mul(mode, *args):
    # print(mode)

    if mode == "sum":
        result = 0
        for num in args:
            result += num

    elif mode == "mul":
        result = 1
        for num in args:
            result *= num
    else:
        print("mode를 입력해주세요")
    print("--------")
    print(result)


# 사용
sum_mul("sum", 1, 23, 45)
sum_mul("mul", 1, 23, 45, 22, 2333)

print("=======================================")


def add_person(hp, **kwargs):
    print(hp)
    print(kwargs)
    print("--------")


add_person("010-1111-1111")
add_person("010-1111-1111", name="정우성")
add_person("010-1111-1111", name="정우성", company="02-1111-111")
add_person("010-1111-1111", birth="2000-01-01", name="정우성", company="02-1111-111")


print("=======================================")


def add_person2(*hp, **kwargs):
    print(hp)  # 폰번호 갯수 가변
    print(hp[0])

    print(kwargs)  # 개인정보 종류 갯수 가변
    print(kwargs["name"])

    print("----------------------")


#
# add_person2("010-1111-1111")
# add_person2("010-1111-1111", "010-2222-2222")
add_person2("010-1111-1111", name="정우성")
add_person2("010-1111-1111", age=24, name="정우성")
add_person2("010-1111-1111", age=24, cname="(주)우리회사", name="정우성")
# add_person2("010-1111-1111", age=24, cname="(주)우리회사", name="정우성", "02-222-222")
add_person2(
    "010-1111-1111",
    "02-222-222",
    age=24,
    cname="(주)우리회사",
    name="정우성",
    aaa="kkkk",
)


x = 1


def func2(a):
    x = 2

    return a + x


print(func2(10))
