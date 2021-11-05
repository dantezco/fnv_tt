import math
import random

import names

from npcgen import SKILLS_STAT

# todo
"""todo Implement a method to stochastically distribute SPECIAL points 
in a way that seem to make sense
todo Implement a method to stochastically distribute skill points based on SPECIAL
    invert SPECIAL dict to values, then get Int % 3 first SPECIALs - Luck to guide"""


class NPC:
    def __init__(self, level: int, initial_special: dict) -> None:
        """Creates a NPC"""
        self.level = level
        self.special = initial_special
        self.hp = 0
        self.sequence = 0
        self.actions_per_turn = 0
        self.skills = dict((skill, 0) for skill, stat in SKILLS_STAT.items())

    def calculate_base_states(self):
        self.hp = self.special["E"] * 20 + 100 + ((self.level - 1) * 5)
        self.sequence = random.randint(1, 10) + self.special["A"]
        self.actions_per_turn = math.ceil(self.special["A"] / 2)

    def invest_skill_points(self):
        intelligence = self.special["I"]
        extra_points = math.ceil(
            self.level * ((intelligence or not intelligence) / 2 + 10)
        )
        self.invest_points(points=extra_points, d=self.skills)

    def invest_special_points(self, points: int):
        self.invest_points(points=points, d=self.special)

    def invest_points(self, points: int, d: dict) -> None:
        while points > 0:
            chunk = random.randint(1, math.ceil(points / 5))
            # todo choose a skill based off the skills
            print(f"x: {points} chunk: {chunk}")
            points -= chunk

    def calculate_initial_skill_level(self, attribute: int) -> int:
        luck = self.special.get("L")
        skill_level = math.ceil(2 + 2 * attribute + ((luck or not luck) / 2))
        return skill_level

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__} lvl {self.level} hp {self.hp} "
            f"seq {self.sequence} acp {self.actions_per_turn}\nSPECIAL "
            f"{self.special}\nSkills {self.skills}"
        )


class Human(NPC):
    """All sentient human NPCs"""

    def __init__(self, level: int, initial_special: dict) -> None:
        super().__init__(level, initial_special)
        self.name = names.get_full_name()
        # todo add markov profile
        # todo invest points
        self.calculate_base_states()
        # self.calculate_initial_skill_level(self.special[stat])
        # self.calculate_initial_skill_level()

    def __repr__(self) -> str:
        return f"{self.name} // " + super().__repr__()


class Animal(NPC):
    """All animals that are not abominations"""


class Robot(NPC):
    """Robots, turrets, etc"""


class Abomination(NPC):
    """Abominations are:

    Aliens
    Centaurs
    Deathclaws
    Night stalkers
    Spore carriers
    Spore plants"""


class Ghoul(NPC):
    """For any ghouls in the Mojave"""


class Ranger(Human):
    """NCR Ranger"""

    def __init__(self, level: int) -> None:
        initial_special = {"S": 9, "P": 3, "E": 7, "C": 5, "I": 7, "A": 9, "L": 5}
        super().__init__(level, initial_special=initial_special)


class VaultDweller(Human):
    """Citizen of a vault"""


class Raider(Human):
    """Any member of any Raider gang"""


class Soldier(Human):
    """Soldiers from the New California Republic"""
