profit = int(input("Введите выручку фирмы: "))
costs = int(input("Введите издержки фирмы: "))
if profit > costs:
    print(f"Фирма работает с прибылью. Рентабельность выручки: {profit / costs}")
    workers = int(input("Введите количество сотрудников: "))
    print(f"Прибыль в расчете на одного сторудника: {(profit - costs) / workers}")
elif profit == costs:
    print("Фирма работает в ноль!")
else:
    print("Фирма работает в убыток!!!")
