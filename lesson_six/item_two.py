class Road:
    weight = 25
    thickness = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate(self):
        result = (self._length * self._width * Road.weight * Road.thickness) / 1000
        print(f'Потребуется {result} тонн.')


my_road = Road(20, 5000)
my_road.calculate()
