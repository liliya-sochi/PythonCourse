from itertools import count, cycle

# а) итератор, генерирующий целые числа, начиная с указанного,
list_int = []
a = int(input("Укажите первое число последовательности: "))
z = int(input("Укажите последнее число последовательности: "))
for i in count(a):
    if i > z:
        break
    print(i)
    list_int.append(i)

# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
print()
print(list_int)
count = 0
for i in cycle(list_int):
    if count >= len(list_int):
        break
    print(i)
    count += 1
