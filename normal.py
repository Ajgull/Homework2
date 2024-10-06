from random import randint


class Person:
    def __init__(self, name: str, health: int, damage: int, armor: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attacked(self, opponent) -> None:

        temp_damage = self.calculate_damage(opponent)
        opponent.health -= temp_damage

        if opponent.health <= 0:
            print(f'{opponent.name} dead')
        else:
            print(f'{opponent.name} has {opponent.health} hp')

    def calculate_damage(self, opponent) -> int:
        if opponent.armor > 0:
            effective_damage = max(self.damage - opponent.armor, 0)
        else:
            effective_damage = self.damage
        return effective_damage

    def is_alive(self) -> bool:
        return self.health > 0


class Enemy(Person):

    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Player(Person):

    def __init__(self, name, health, damage, armor):
        super().__init__(name, health, damage, armor)


class Game:

    def __init__(self):
        self.player = Player('player', 100, 10, 4)

        self.enemy = Enemy('boss', 100, 0, 0)

    def start(self) -> None:
        while (self.player.is_alive() != 0) and (self.enemy.is_alive() != 0):
            temp = randint(1, 2)
            if temp % 2 == 0:
                self.player.attacked(self.enemy)
            else:
                self.enemy.attacked(self.player)

        print('Game is over')
