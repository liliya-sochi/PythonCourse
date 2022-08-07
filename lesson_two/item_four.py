x = input("Введите слова через пробел: ")
s = x.split(" ")

for i, item in enumerate(s):
    print(f"{i + 1}. {item[:10]}")
