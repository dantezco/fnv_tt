import random


class Dice:
    def __init__(self, description: str = "1d6"):
        self._description = description

    def roll(self) -> tuple:
        tokens = self._description.split()
        rolled_tokens = [self._try_rolling_dice(t) for t in tokens]
        dice_expression = "".join([str(rt) for rt in rolled_tokens])
        dice_value = eval(dice_expression)
        return dice_value

    def _try_rolling_dice(self, dice: str):
        is_dice = "d" in dice
        if is_dice:
            return self._roll_dice(dice)
        else:
            return dice

    def _roll_dice(self, dice: str):
        parsed_dice = [int(t) for t in dice.split("d")]
        result = 0
        for value in range(parsed_dice[0]):
            result += random.randint(1, parsed_dice[1])
        return result

    def __str__(self):
        return f"{self._description}"


arr = []
dice = Dice("2d100 * 3")
print(f"TESTING << {dice} >>\n")
for i in range(10000):
    roll_value = dice.roll()
    arr.append(roll_value)

# frequency of each roll
freqs = {}
for el in arr:
    if el in freqs:
        freqs[el] += 1
    else:
        freqs[el] = 1

# grouping the results based on the amount of times each value was rolled
group_freqs = {}
for el in freqs:
    if freqs[el] in group_freqs:
        group_freqs[freqs[el]] += [el]
    else:
        group_freqs[freqs[el]] = [el]

gf_keys = list(group_freqs.keys())
gf_keys.sort()

average = 0
cases = 0
for key in gf_keys[-10:]:
    sorted_results = group_freqs[key]
    sorted_results.sort()
    average += sum(sorted_results)
    cases += len(sorted_results)
    print(f"rolled {str(key).zfill(2)} times:\n {sorted_results} ")

print(f"\naverage of most repeated {cases} results is {int(average / cases)}")
