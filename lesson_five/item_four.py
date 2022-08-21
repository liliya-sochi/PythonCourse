import json

with open("salary.json", encoding='utf-8') as my_file:
    salary = json.load(my_file)
    print(type(salary))
    print("Сотрудники, зарабатывающие менее  20000$ в год: ")
    for keys, values in salary.items():
        if values < 20000:
            print(keys)
    print(f"Средняя заработная плата = {sum(salary.values())/len(salary)}$ в год.")
