class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} поехала.'

    def stop(self):
        return f'{self.name} остановилась.'

    def turn(self, direction):
        return f'{self.name} повернула в направлении {direction}.'

    def show_speed(self):
        return f'Текущая скорость автомобиля {self.name} составляет {self.speed}.'


class TownCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость городского автомобиля {self.name} составляет {self.speed}.')

        if self.speed > 60:
            return f'Скорость автомобиля {self.name} выше, чем это позволено для городского автомобиля.'
        else:
            return f'Скорость автомобиля {self.name} нормальная для городского автомобиля.'


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Текущая скорость рабочего автомобиля {self.name} составляет {self.speed}.')

        if self.speed > 40:
            return f'Скорость автомобиля {self.name} выше, чем это позволено для рабочего автомобиля.'
        else:
            return f'Скорость автомобиля {self.name} нормальная для рабочего автомобиля.'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def sport(self):
        if self.is_police:
            return f'Автомобиль {self.name} является спортивным.'
        else:
            return f'Автомобиль {self.name} не является спортивным.'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'Автомобиль {self.name} является полицейским.'
        else:
            return f'Автомобиль {self.name} не является полицейским.'


HONDA = TownCar(35, 'Красная', 'Honda', False)
NISSAN = WorkCar(80, 'Белый', 'Nissan', True)
SUBARU = SportCar(100, 'Чёрный', 'Subaru', False)
TOYOTA = PoliceCar(110, 'Синяя', 'Toyota', True)

print(HONDA.show_speed())
print(NISSAN.show_speed())
print(SUBARU.show_speed())
print(TOYOTA.show_speed())

print(NISSAN.turn("направо"))
print(f'Когда {HONDA.turn("налево")}, то {SUBARU.stop()}')
print(f'{NISSAN.go()} со скоростью {NISSAN.show_speed()}')
print(f'{NISSAN.name} цвета {NISSAN.color}')
print(f'{SUBARU.name} полицейская машина? {SUBARU.is_police}')
print(f'{NISSAN.name} полицейская машина? {NISSAN.is_police}')
