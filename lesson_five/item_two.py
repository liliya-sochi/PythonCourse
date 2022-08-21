lines = 0
words = 1

with open("file.txt", "r", encoding='utf-8') as my_file:
    for line in my_file:
        print(line.replace('\n', ''))
        for n in line:
            if n == " ":
                words += 1
        lines += 1
        print(f"Количество слов в строке {lines} = {words} \n")
        count_words = 1
    print(f"В файле {lines} строк(и)")
