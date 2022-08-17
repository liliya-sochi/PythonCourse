from itertools import count


def fact(n):
    factorial = 1
    for i in count(1):
        if i > n:
            break
        factorial = factorial * i
        yield factorial


n = int(input("Укажите целое неотрицательное число: "))
x = 0
for el in fact(n):
    x += 1
    print(f"!{x} = {el}")
