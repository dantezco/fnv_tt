import re
import random
import copy

    
class LatexTable:
    def __init__(self, name: str) -> None:
        self._name = name
        self._data = []
        self._index = 0

    def parse(self, path: str, regex: str) -> None:
        with open(path, 'r') as file:
            for line in file.readlines():
                line_parsed = re.match(regex, line)
                if line_parsed:
                    self._data.append(line_parsed.groups())

    def print(self):
        for line in self._data:
            print(line)

    def __iter__(self):        
        return self

    def __next__(self):
        if self._index < len(self._data):
            result = self._data[self._index]
            self._index += 1
            return result
        raise StopIteration

    def __str__(self):
        return f'Table {self._name} with {len(self._data)} lines of data'


class Enemy:
    def __init__(self, hp: int, dt: int, name: str) -> None:
        self._hp = hp
        self._dt = dt
        self._name = name

    def is_dead(self) -> None:
        return self._hp <= 0

    def hurt(self, amount) -> None:
        self._hp -= amount

    def __str__(self) -> str:
        return self._name


class Dice:
    def __init__(self, description: str = '1d6') -> None:
        self._description = description
    
    def roll(self) -> tuple:
        tokens = self._description.split()
        dice_expression = ""
        for token in tokens:
            is_dice = re.match('[0-9]+d[0-9]+', token)
            if is_dice:
                dice_expression += str(self._roll_dice(dice=token))
            else:
                dice_expression += token
        dice_value = eval(dice_expression)
        return dice_value
    
    def _roll_dice(self, dice: str) -> int:
        parsed_dice = [int(t) for t in dice.split('d')]
        result = 0
        for value in range(parsed_dice[0]):
            result += random.randint(1, parsed_dice[1])
        return result

    def __str__(self) -> str:
        return f"{self._description}"


class Weapon:
    def use(self):
        pass


class GunEW(Weapon):
    def __init__(self, dice: str, player_skill: int, name: str) -> None:
        self._dice = Dice(description=dice)
        self._player_skill = player_skill
        self._name = name

    def use(self) -> int:
        return int(self._dice.roll() * ((50 + self._player_skill) / 100))

    def __str__(self) -> str:
        return f'{self._name} with skill {self._player_skill}'


def attacks_until_kill(enemy: Enemy, weapon: Weapon) -> int:
    turns = 0
    while not enemy.is_dead():
        turns += 1
        damage_done = weapon.use()
        enemy.hurt(amount=damage_done)
    return turns


def frequency_turns_to_kill(monster: Enemy, weapon: Weapon, experiments: int) -> dict:
    freqs = {}
    for i in range(experiments):
        try:
            enemy = copy.deepcopy(monster)
            turns_to_kill = attacks_until_kill(enemy=enemy, weapon=weapon)
            if turns_to_kill in freqs:
                freqs[turns_to_kill] += 1
            else:
                freqs[turns_to_kill] = 1
        except Exception as error:
            print(error)
            continue
    return freqs


def get_parsed_latex_table(regex: str, name: str, path: str) -> LatexTable:
    latex_table = LatexTable(name=name)
    latex_table.parse(path=path, regex=regex)
    return latex_table


def create_creatures_table() -> list:
    creatures = get_parsed_latex_table(regex='^([\w\s\-\*]+)& ([\d\.]+) & ([\d\.]+).*\\\\', name='Enemies or creatures', path='../rules/table_creatures.tex')
    table = []
    for creature in creatures:
        table.append(Enemy(hp=int(creature[1]), dt=int(creature[2]), name=creature[0].strip()))    
    return table 


def create_fireable_weapons_table(paths: list, player_skills: list) -> list:
    table = []
    for path in paths:
        weapons = get_parsed_latex_table(regex='^([\w\s\-\*]+)& [\d\.]+ & [\d\.]+ & ([\w\s\+\*]+) \\\\', name='Guns or Energy Weapons', path=path)
        for weapon in weapons:
            for skill in player_skills:
                table.append(GunEW(dice=weapon[1].strip(), player_skill=skill, name=weapon[0].strip()))
    return table

def log_frequencies(guns_ew: list, enemies: list, experiments: int) -> None:
    for enemy in enemies:
        with open(f'./freqs/{enemy}.csv', 'w') as freq_file:
            most_items = 0
            lines = []
            for weapon in guns_ew:
                print(f'{enemy} - {weapon}')
                ttk = frequency_turns_to_kill(monster=enemy, weapon=weapon, experiments=experiments)
                tokens = [f'{weapon}']
                for key, value in sorted(ttk.items(), key=lambda x: x[0]):
                    tokens.append(f'{value}')
                line = f'{",".join(tokens)}'
                amount_turns = line.count(',')
                if amount_turns > most_items:
                    most_items = amount_turns
                lines.append(line)
            header = f'Name,' + f",".join(f'{x+1} turns' for x in range(most_items))
            freq_file.write('\n'.join([header] + lines))    

enemies = create_creatures_table()

weapons_paths = ['../rules/table_pistols.tex',
                 '../rules/table_rifles.tex',
                 '../rules/table_smg.tex',
                 '../rules/table_shotguns.tex',
                 '../rules/table_heavyw.tex',
                 '../rules/table_energyp.tex',
                 '../rules/table_energyr.tex',
                 '../rules/table_energyhw.tex',
                 ]

experiments = 1000
player_skills = [25, 100]
guns_ew = create_fireable_weapons_table(paths=weapons_paths, player_skills=player_skills)
log_frequencies(guns_ew=guns_ew, enemies=enemies, experiments=experiments)
