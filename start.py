from easy import TownCar, PoliceCar, SportCar
from normal import Game
from hard import Factory


def first():
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


def second():
    game = Game()
    game.start()


def third():
    t = Factory()
    n = t.make_toy('Mickey', 'white', 'film')
    print(n.__str__())
    print()
    e = t.make_toy('default', 'red', 'ball')
    print(e.__str__())
    print()
    r = t.make_toy('bmv', 'black', 'car')
    print(r.__str__())
