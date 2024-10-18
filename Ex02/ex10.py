def plus(a, b):
    sum = a + b
    return sum


result = plus(5, 3)
print(result)


print("--------------------------")


def sum_many(*args):
    sum = 0
    for num in args:
        sum = sum + num
    return sum


print(sum_many(1, 2))
print(sum_many(1, 2, 3, 4, 5))


print("===========================")


def sum_mul(mode, *args):
    if mode == "sum":
        result = 0
        for i in args:
            result = result + i
    elif mode == "mul":
        result = 1
        for i in args:
            result = result * i
    return result


print(sum_mul("sum", 1, 2, 3, 4, 5))
print(sum_mul("mul", 2, 3))
