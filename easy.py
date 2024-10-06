class Car:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed: int, color: str, name: str, is_police: bool = False) -> None:
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def good_speed(self) -> bool:
        if (self.speed >= 0) and (self.speed <= 80):
            print(f'{self.name} im moving with good speed {self.speed}')
            return True
        else:
            print(f'{self.name} im moving with too high speed {self.speed}')
            return False

    def go(self) -> None:
        print(f'{self.color} {self.name} is moving with speed {self.speed}')

    def stop(self) -> None:
        print(f'{self.name} stopped')

    def turn(self, direction: str) -> bool:
        if direction in ['left', 'right', 'forward', 'back']:
            print(f'{self.name} go {direction}')
            return True
        else:
            print(f'{self.name} go wrong way')
            return False


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name)

    def go(self) -> None:
        print('Town car move slow')


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name)


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str) -> None:
        super().__init__(speed, color, name, is_police=True)

    def sound(self) -> None:
        print('Sound of police car')
