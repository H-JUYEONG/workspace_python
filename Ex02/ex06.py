# tuple -> list===========================

t = (1, 2, 3)  # 읽기전용
print(type(t))
# t[1] = 100       #변경안됨 튜플확인

a_list = list(t)
print(a_list)
print(type(a_list))  # list
a_list[1] = 100
print(a_list)

# list --> tuple===========================
a = [1, 2, 3, 1]
print(type(a))

t_tuple = tuple(a)
print(t_tuple)
# t_tuple[1] = 999


# tuple --> set===========================
t = (1, 2, 3, 1)
print(t)

s_set = set(t)
print(s_set)
