import copy

from latex_table import LatexTable
from entities import Enemy, Weapon


class CombatSimulation:
    def __init__(self, amt_experiments: int):
        self._experiments = amt_experiments

    @staticmethod
    def _count_attacks_until_kill(enemy: Enemy, weapon: Weapon) -> int:
        turns = 0
        while not enemy.is_dead():
            turns += 1
            damage_done = weapon.use()
            enemy.hurt(amount=damage_done)
        return turns

    def _run_experiments(
        self, monster: Enemy, weapon: Weapon, experiments: int
    ) -> dict:
        results = {}
        for i in range(experiments):
            try:
                enemy = copy.deepcopy(monster)
                weapon.reset_dice()
                turns_to_kill = self._count_attacks_until_kill(
                    enemy=enemy, weapon=weapon
                )
                if turns_to_kill in results:
                    results[turns_to_kill] += 1
                else:
                    results[turns_to_kill] = 1
            except Exception as error:
                print(f"Error: {error}")
                results = {}
                break
        return results

    def _format_result_csv(self, results: dict, weapon: Weapon) -> list:
        tokens = [f"{weapon}"]
        for key, value in sorted(results.items(), key=lambda x: x[0]):
            tokens.append(f"{value}")

        line = f'{",".join(tokens)}'
        return line

    def _log_results(self, results: list, enemy: Enemy):
        most_ttk = 0
        for result in results:
            current_max_ttk = result.count(",")
            if current_max_ttk > most_ttk:
                most_ttk = current_max_ttk
        header = f"Name," + f",".join(f"{x + 1} turns" for x in range(most_ttk))
        with open(f"results/{enemy} DT {enemy.get_dt()}.csv", "w") as freq_file:
            freq_file.write("\n".join([header] + results))

    def _create_creatures_table(self) -> list:
        creatures = LatexTable(
            name="Enemies or creatures",
            regex=r"^([\w\s\-\*]+)& ([\d\.]+) & ([\d\.]+).*\\\\",
            path="../rules/table_creatures.tex",
        )
        table = []
        test_creatures = [
            "Golden gecko",
            "Deathclaw",
            "Night stalkers",
            "Giant radscorpion",
            "Hardened Mister Gutsy",
            "Deathclaw alpha male",
        ]
        for creature in creatures:
            if creature[0].strip() in test_creatures:
                table.append(
                    Enemy(
                        hp=int(creature[1]),
                        dt=int(creature[2]),
                        name=creature[0].strip(),
                    )
                )
        return table

    def _create_weapons_table(self) -> list:
        table = []
        files_paths = [
            "../rules/table_pistols.tex",
            "../rules/table_rifles.tex",
            "../rules/table_smg.tex",
            "../rules/table_shotguns.tex",
            "../rules/table_heavyw.tex",
            "../rules/table_energyp.tex",
            "../rules/table_energyr.tex",
            "../rules/table_energyhw.tex",
        ]

        for path in files_paths:
            weapons = LatexTable(
                name="Guns or Energy Weapons",
                regex=r"^([\w \-\*]+) & [\w ]+ & ([\w ]+) & ([\d\.]+) & ([\w\s\+\*]+) \\\\",
                path=path,
            )
            for weapon in weapons:
                table.append(Weapon(dice=weapon[3].strip(), name=weapon[0].strip()))
        return table

    def main(self):
        enemies = self._create_creatures_table()
        weapons = self._create_weapons_table()

        for enemy in enemies:
            print(enemy)
            results = []
            for weapon in weapons:
                experiments_result = self._run_experiments(
                    monster=enemy, weapon=weapon, experiments=self._experiments
                )
                formatted_result = self._format_result_csv(
                    results=experiments_result, weapon=weapon
                )
                results.append(formatted_result)
            self._log_results(results=results, enemy=enemy)


if __name__ == "__main__":
    cs = CombatSimulation(amt_experiments=1000)
    cs.main()
