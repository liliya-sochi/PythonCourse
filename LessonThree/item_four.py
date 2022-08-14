def my_func(x, y):
    try:
        if y < 0:
            res = 1
            for i in range(y, 0):
                res = res * x
            res = 1 / res
            return res
        else:
            return "Число должно быть отрицательным!"
    except TypeError:
        return "Функция принимает только числа!"
    except ZeroDivisionError:
        return "На ноль делить незьзя!"

