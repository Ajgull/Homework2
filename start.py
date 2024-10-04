from easy import TownCar, PoliceCar, SportCar


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
    if not s.good_speed():
        s.stop()
