x = input("Введите целые числа через пробел: ")
a = x.split(" ")

i = 0

if len(a) % 2 == 0:
    while i < len(a):
        a[i], a[i + 1] = a[i + 1], a[i]
        i += 2
else:
    while i < len(a) - 1:
        a[i], a[i + 1] = a[i + 1], a[i]
        i += 2

print(f"Результат: {a}")
