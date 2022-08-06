seconds = int(input("Введите время в секундах: "))
seconds = seconds % (24 * 3600)
hours = seconds // 3600
seconds %= 3600
minutes = seconds // 60
seconds %= 60
print("Результат: %02d:%02d:%02d" % (hours, minutes, seconds))
