from random import choice


class Person:
    def __init__(self, name: str, health: int, damage: int, armor: int) -> None:
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def attack(self, opponent: 'Person') -> None:
        temp_damage = self._calculate_damage(opponent)
        opponent.health -= temp_damage

        if opponent.health <= 0:
            print(f'{opponent.name} dead')
        else:
            print(f'{opponent.name} has {opponent.health} hp')

    def _calculate_damage(self, opponent: 'Person') -> int:
        if opponent.armor > 0:
            effective_damage = max(self.damage - opponent.armor, 0)
        else:
            effective_damage = self.damage
        return effective_damage

    def is_alive(self) -> bool:
        return self.health > 0


class Enemy(Person):
    def __init__(self, name: str, health: int, damage: int, armor: int) -> None:
        super().__init__(name, health, damage, armor)


class Player(Person):
    def __init__(self, name: str, health: int, damage: int, armor: int) -> None:
        super().__init__(name, health, damage, armor)


class Game:
    def __init__(self) -> None:
        self.player = Player('player', 100, 10, 4)

        self.enemy = Enemy('boss', 100, 0, 0)

    def start(self) -> None:
        while self.player.is_alive() and self.enemy.is_alive():
            if choice([True, False]):
                self.player.attack(self.enemy)
            else:
                self.enemy.attack(self.player)

        print(f'Game is over. {self.player.name if self.player.is_alive() else self.enemy.name} won')
