from easy import PoliceCar, SportCar, TownCar
from hard import Factory
from normal import Game


def first() -> None:
    t = TownCar(60, 'red', 'Town car')
    t.go()
    t.turn('right')
    t.good_speed()

    p = PoliceCar(100, 'white', 'Police car')
    p.turn('diagonal')

    if not (p.good_speed()):
        p.sound()

    s = SportCar(120, 'black', 'ferrari')
    if not p.good_speed():
        s.stop()


def second() -> None:
    game = Game()
    game.start()


def third() -> None:
    t = Factory()
    n = t.make_toy('Mickey', 'white', 'film')
    print(n)
    print()
    e = t.make_toy('default', 'red', 'ball')
    print(e)
    print()
    r = t.make_toy('bmw', 'black', 'car')
    print(r)


def main() -> None:
    print('==========easy task==========')
    first()
    print()
    print('==========normal task==========')
    second()
    print()
    print('==========hard task==========')
    third()


if __name__ == '__main__':
    main()
