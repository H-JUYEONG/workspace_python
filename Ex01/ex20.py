animal_list = ["cat", "cow", "tiger"]

for animal in animal_list:
    print(animal)
    print("------")


print("=====================")

for no in range(10):
    print(no)
print("---------------------")

for no in range(5, 10):
    print(no)
print("---------------------")

for no in range(1, 10, 3):
    print(no)

print("---------------------")
for no in range(0, 9, 2):
    print(no)

print("---------------------")
for no in range(5, -6, -1):
    print(no)


print("--------구구단전체--------")
for dan in range(2, 10, 1):
    for i in range(1, 10, 1):
        print(f"{dan} * {i} = {dan*i}")


print("--------구구단--------")
dan2 = int(input("단을 입력하세요\n"))
for i in range(1, 10, 1):
    print(f"{dan2} * {i} = {dan2*i}")
