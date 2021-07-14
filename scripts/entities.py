from dice import Dice

class Enemy:
    def __init__(self, hp: int, dt: int, name: str) -> None:
        self._hp = hp
        self._dt = dt
        self._name = name

    def is_dead(self) -> bool:
        return self._hp <= 0

    def hurt(self, amount) -> None:
        self._hp -= amount

    def get_dt(self) -> int:
        return self._dt

    def __str__(self) -> str:
        return f"{self._name} HP {self._hp}"


class Weapon:
    def __init__(self, dice: str, name: str) -> None:
        self._dice = Dice(description=dice)
        self._name = name

    def use(self) -> int:
        damage_done = int(self._dice.roll())
        return damage_done #* ((50 + self._player_skill) / 100))

    def reset_dice(self) -> None:
        self._dice.reset_cumulative_damage()

    def __str__(self) -> str:
        return f'{self._name}'

