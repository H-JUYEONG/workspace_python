t = (1, 2, 3)  # t = 1, 2, 3   # t = tuple([1,2,3])
print(t, type(t))

t = 1, 2, "python"
print(t, type(t))

print(t[-2], t[-1], t[0], t[1], t[2])
print(t[1:3])
print(t[:])

print(t * 2)
print(t + (3, 4, 5))  # t = t + (3, 4, 5)  이렇게 해야 합쳐짐
print(t)
print(len(t))
print(5 in t)
