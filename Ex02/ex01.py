test_list = [1, 12, 123, 1234]

print(test_list[0], test_list[3])
print(test_list[-1], test_list[-2])

print(test_list[1:3])

print(test_list + [100, 200, 300])
print((test_list))


a = [1, 12, 123, 1234]
print(a)

a[1:1] = "a"
print(a)

print("--------------------------------------")

a = [1, 12, 123, "hello", 3.14, 1000]
print(a)

# 추가
a.append(5)
print(a)

a.insert(3, 1000)
print(a)

a.extend([6, 7, 8])
print(a)

# 제거
a.remove(1000)
print(a)

a.pop(2)
print(a)

a.pop()
# del(a[4])

print("--------------------------------------")

b = [1, 123, 1000, 12, 1000]
print(b)

# 카운트
print(b.count(1000))

# 뒤집기
b.reverse()
print(b)

# 정렬
b.sort()
print(b)

# index 찾기
print(b.index(1000))
