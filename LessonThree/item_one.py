def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Деление на ноль недопустимо!")


try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    print("Результат:", division(a, b))
except ValueError:
    print("Вы ввели не числа!")

