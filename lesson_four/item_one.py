import sys

f_obj, name_v, rate_v, hours_v = sys.argv
print(f_obj)


def salary(rate, hours):
    try:
        print(f"Сотрудник {name_v} заработал {int(rate) * int(hours) * 1.25}.")
    except TypeError:
        print("Несоответствующий тип!")
        exit()


salary(rate_v, hours_v)
