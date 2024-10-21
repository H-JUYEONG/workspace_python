color_list = ["reds", "orange", "yellow", "green", "blue"]

for color in color_list:
    print(color)


for index, color in enumerate(color_list):
    if index > 3:
        break
    else:
        print(index, color)
