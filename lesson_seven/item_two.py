class Textil:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square_coat(self):
        return self.width / 6.5 + 0.5

    def get_square_jacket(self):
        return self.height * 2 + 0.3

    @property
    def get_square_full(self):
        return str(f'Общая площадь ткани: {(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}.')


class Coat(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_coat = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f'Площадь на пальто: {self.square_coat}.'


class Jacket(Textil):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_jacket = round(self.height * 2 + 0.3)

    def __str__(self):
        return f'Площадь на костюм: {self.square_jacket}.'


coat = Coat(2, 4)
jacket = Jacket(1, 2)
print(coat)
print(jacket)
print(coat.get_square_full)
print(jacket.get_square_full)
