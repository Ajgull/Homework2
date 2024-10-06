class Toy:
    def __init__(self, name: str, color: str, type_of_toy: str) -> None:
        self.name = name
        self.color = color
        self.type_of_toy = type_of_toy

    def __str__(self) -> str:
        return f'Игрушка : {self.name}, цвет {self.color}, тип {self.type_of_toy}'

    def play(self) -> None:
        pass


class CarToy(Toy):
    def __init__(self, name: str, color: str, type_of_toy: str = 'car') -> None:
        super().__init__(name, color, type_of_toy)

    def play(self) -> str:
        return 'Звук работающай машинки'


class BallToy(Toy):
    def __init__(self, name: str, color: str, type_of_toy: str = 'ball') -> None:
        super().__init__(name, color, type_of_toy)

    def play(self) -> str:
        return 'Звук прыгающего мяча'


class DollToy(Toy):
    def __init__(self, name: str, color: str, type_of_toy: str = 'doll') -> None:
        super().__init__(name, color, type_of_toy)

    def play(self) -> str:
        return 'Звук кукол'


class AnimalToy(Toy):
    def __init__(self, name: str, color: str, type_of_toy: str) -> None:
        super().__init__(name, color, type_of_toy)

    def play(self) -> str:
        return 'Звук животного'


class Factory:
    def make_toy(self, name: str, color: str, type_of_toy: str) -> Toy:
        if type_of_toy == 'car':
            t = CarToy(name, color, type_of_toy)
        elif type_of_toy == 'doll':
            t = DollToy(name, color, type_of_toy)
        elif type_of_toy == 'ball':
            t = BallToy(name, color, type_of_toy)
        else:
            print(f'Мы не производим игрушки типа {type_of_toy}')
            print('Тогда мы сделает игрушку типа Animal toy')
            t = AnimalToy(name, color, type_of_toy)

        self.buy_materials()
        self.sewing()
        self.coloring()

        print(f'Игрушка {name} изготовлена')
        return t

    def buy_materials(self) -> None:
        print('Материалы для игрушки закуплены')

    def sewing(self) -> None:
        print('Начат пошив игрушки')

    def coloring(self) -> None:
        print('Покраска игрушки начата')
