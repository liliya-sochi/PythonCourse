class OfficeEquipment:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Модель устройства': self.name, 'Цена за единицу': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def reception(self):
        try:
            unit = input(f'Введите наименование: ')
            unit_p = int(input(f'Введите цену за единицу: '))
            unit_q = int(input(f'Введите количество: '))
            unique = {'Модель устройства': unit, 'Цена за единицу': unit_p, 'Количество': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Текущий список: \n {self.my_store}')
        except:
            return f'Не верно ввели данные!'
        print(f'Для выхода введите - Q, продолжение - Enter!')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад: \n {self.my_store_full}')
            return f'Конец!'
        else:
            return OfficeEquipment.reception(self)


class Printer(OfficeEquipment):
    def to_print(self):
        return f'Напечатать что-то {self.numb} раз!'


class Scanner(OfficeEquipment):
    def to_scan(self):
        return f'Отсканировать что-то {self.numb} раз!'


class Copier(OfficeEquipment):
    def to_copier(self):
        return f'Скопировать что-то {self.numb} раз!'


unit_1 = Printer('hp', 2000, 5, 10)
unit_2 = Scanner('Canon', 1200, 5, 10)
unit_3 = Copier('Xerox', 1500, 1, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_2.to_scan())
print(unit_3.to_copier())
