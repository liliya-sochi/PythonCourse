data = int(input("Введите целое положительное число: "))
result = -1
while data > 10:
    temp = data % 10
    data //= 10
    if temp > result:
        result = temp
print(result)
