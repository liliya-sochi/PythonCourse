primary_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = [el for el in primary_list if primary_list.count(el) == 1]
print(result_list)
