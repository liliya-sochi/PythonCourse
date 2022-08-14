def my_func1(a, b, c):
    args = {a, b, c}
    return "Результат:", sum(sorted(list(args), reverse=True)[:2])


def my_func2(a, b, c):
    if a >= c and b >= c:
        return "Результат:", a + b
    elif a > b and a < c:
        return "Результат:", a + c
    else:
        return "Результат:", b + c

