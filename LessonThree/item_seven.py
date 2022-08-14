def int_func(string):
    list = string.split()
    result = []
    for el in list:
        result.append(el.title())
    print(*result)

