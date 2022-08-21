my_file = open("file.txt", 'w', encoding='utf-8')
lines = []

while True:
    line = input("Введите текст или нажмите Enter для завершения: ")
    if line != '':
        lines.append(line + "\n")
    else:
        break
my_file.writelines(lines)

with open("file.txt", "r", encoding='utf-8') as my_file:
    content = my_file.readlines()
    print(content)

with open("file.txt", "r", encoding='utf-8') as my_file:
    for line in my_file:
        print(line)
