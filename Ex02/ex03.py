# 딕션어리  키-값

# =딕션어리 생성==========================================
a = {}

# "r38" "빅데이터반"
a["r38"] = "빅데이터반"
a["r32"] = "풀스택반"
a["r30"] = "진소영"
print(a)
print(type(a))  # <class 'dict'>

d = {"basketball": 5, "soccer": 11, "baseball": 9}
d["volleyball"] = 6
print(d)

# =딕션어리 값 출력==========================================
print(a["r30"])
print(d["soccer"])
# print(d.get("soccer"))

# =딕션어리 값 삭제->키==========================================
print(d)
# del(d["soccer"])
d.pop("soccer")
print(d)

print("#=딕션어리 값 삭제(전체)==================================")
d = {"basketball": 5, "soccer": 11, "baseball": 9}
print(d)

# d = {}
d.clear()
print(d)


print("#=찾기==================================")
d = {"basketball": 5, "soccer": 11, "baseball": 9}
print(d)
print(len(d))
print("soccer" in d)
print("soccer" not in d)


print("#=딕션어리의 키들을 리스트로 반환======================")
d = {"basketball": 5, "soccer": 11, "baseball": 9}
keys = d.keys()
print(keys, type(keys))

for key in keys:
    print(key)
    print(d[key])
    # print( f"{key} -> {d[key]}" )


print("#=딕션어리의 값들을 리스트로 반환======================")

value_list = d.values()
print(value_list)
print(type(value_list))

for value in value_list:
    print(value)


# {'basketball': 5, 'soccer': 11, 'baseball': 9}

# [{'basketball': 5}, {'soccer': 11}, {'baseball': 9} ]

play_list = d.items()
print(play_list, type(play_list))
print(type(list(play_list)))
