n = int(input("Введите число: "))
step = 0
temp = 0
result = 0
while step < n:
        temp = temp * 10 + n
        result += temp
        step = step + 1
print(result)
