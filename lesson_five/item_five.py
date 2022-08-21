numbers = "0 1 2 3 4 5 6 7 8 9"
result = 0

with open("five.txt", "w", encoding='utf-8') as my_file:
    my_file.write(numbers)

with open("five.txt", encoding='utf-8') as my_file:
    content = my_file.read().split(" ")
    for i in content:
        result += int(i)
    print(f"Сумма чисел = {result}")
