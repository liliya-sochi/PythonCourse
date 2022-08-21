translate = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("input_file.txt", encoding='utf-8') as english:
    for line in english:
        for key in translate.keys():
            line = line.replace(key, translate[key])
        print(line)
        with open("output_file.txt", "a") as russian:
            russian.write(f"\n {line}")
