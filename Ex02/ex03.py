a = {}  # 생성방법

# 추가
a["r38"] = "빅데이타"
a["r32"] = "c언어"
print(a)

# 생성방법
d = {"basketball": 5, "soccer": 11, "baseball": 9}
d["volleyball"] = 6
print(d)

# 값출력
print(d["basketball"])
print(d.get("basketball"))

d = {"basketball": 5, "soccer": 11, "baseball": 9}
del d["basketball"]
print(d)

d = {"basketball": 5, "soccer": 11, "baseball": 9}
d = {}
print(d)

d = {"basketball": 5, "soccer": 11, "baseball": 9}
d.clear()
print(d)

print(type(d))

print(len(d))

print("soccer" in d)
print("volleyball" not in d)


print("---------------------------")

d = {"basketball": 5, "soccer": 11, "baseball": 9}
keys = d.keys()
print(keys)
print(type(keys))

for key in keys:
    print("{0}:{1}".format(key, d[key]))
