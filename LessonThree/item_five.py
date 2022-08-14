def my_sum():
    sum = 0
    exit = False
    while exit == False:
        number = input("Введите числа через пробез или q для выхода: ").split()
        result = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                exit = True
                break
            else:
                result += int(number[el])
        sum += result
        print(f"Текущая сумма чисел: {result}")
    print(f"Общая сумма чисел: {sum}")

