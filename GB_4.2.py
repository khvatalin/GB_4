first_list = [150, 3, 4, 18, 29, 17, 202]
second_list = [el for num, el in enumerate(first_list) if first_list[num - 1] < first_list[num]]
print(f'Первый список {first_list}')
print(f'Второй список {second_list}')
