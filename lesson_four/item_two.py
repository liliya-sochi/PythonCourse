primary_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# вариант без lc
list_1 = []
for el in range(1, len(primary_list)):
    if primary_list[el] > primary_list[el - 1]:
        list_1.append(primary_list[el])
print(list_1)

# вариант с lc
list_2 = [primary_list[el] for el in range(1, len(primary_list)) if primary_list[el] > primary_list[el - 1]]
print(list_2)
