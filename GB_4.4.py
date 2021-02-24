first_list = [24, 24, 28, 92, 1, 92, 18, 14, 71]
second_list = [el for el in first_list if first_list.count(el) < 2]
print(second_list)