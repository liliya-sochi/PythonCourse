class Stationery:
    def __init__(self, title):
        self.title = title

    @staticmethod
    def draw():
        print('Запуск отрисовки!')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}. Класс Pen.')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}. Класс Pencil.')


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка {self.title}. Класс Handle.')


my_pen = Pen("ручкой")
my_pencil = Pencil("карандашом")
my_handle = Handle("маркером")

my_pen.draw()
my_pencil.draw()
my_handle.draw()
