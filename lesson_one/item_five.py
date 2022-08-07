profit = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if profit > costs:
    print("Фирма работает с прибылью!")
elif profit == costs:
    print("Фирма работает в ноль!")
else:
    print("Фирма работает в убыток!!!")
