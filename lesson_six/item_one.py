from time import sleep


class TrafficLight:
    __color = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    @staticmethod
    def running():
        for key, value in TrafficLight.__color.items():
            print(f'Светофор переключился в режим {key}')
            sleep(value)


traffic_light = TrafficLight()
traffic_light.running()
