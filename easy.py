class TownCar:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, stroke):
        print(f'{self.name} move {stroke}')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, stroke):
        print(f'{self.name} go {stroke}')


class SportCar:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, stroke):
        print(f'{self.name} move {stroke}')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, stroke):
        print(f'{self.name} go {stroke}')


class WorkCar:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, stroke):
        print(f'{self.name} move {stroke}')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, stroke):
        print(f'{self.name} go {stroke}')


class PoliceCar:
    speed = 0
    color = ''
    name = ''
    is_police = False

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, stroke):
        print(f'{self.name} move {stroke}')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, stroke):
        print(f'{self.name} go {stroke}')

