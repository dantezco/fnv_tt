import re
import random

class Dice:
    def __init__(self, description: str = '1d6') -> None:
        d, cd = self._parse(text=description)
        self._dice = d
        self._cumulative_dice = cd
        self._cumulative_damage = []

    def reset_cumulative_damage(self):
        self._cumulative_damage = []

    def _parse(self, text: str) -> tuple:
        has_cumulative_damage = "plus cumulative" in text

        end_dice_text = text.find("plus cumulative") if has_cumulative_damage else len(text)
        start_cumulative_dice = end_dice_text + 15

        dice_text = text[:end_dice_text]
        cumulative_text = text[start_cumulative_dice:]

        dice = dice_text.split()
        cumulative_dice = cumulative_text.split()

        return dice, cumulative_dice

    def parse_dice_token(self, token: str) -> str:
        expression = ""
        token_is_dice = "d" in token
        if token_is_dice:
            expression += str(self._roll_dice(dice=token))
        else:
            expression += token
        return expression

    def roll(self):
        dice_expression = ""
        for token in self._dice:
            parsed_value = self.parse_dice_token(token=token)
            dice_expression += parsed_value
        dice_value = eval(dice_expression)
        
        cumulative_dice_expression = ""
        if self._cumulative_dice:
            for token in self._cumulative_dice:
                cumulative_dice_expression += self.parse_dice_token(token=token)
            cumulative_value = eval(cumulative_dice_expression)
            self._cumulative_damage.append(cumulative_value)
            cumulative_value = sum(self._cumulative_damage)
        else:
            cumulative_value = 0
        value = dice_value + cumulative_value

        return value

    def _roll_dice(self, dice: str) -> int:
        parsed_dice = [int(t) for t in dice.split('d')]
        result = 0
        for value in range(parsed_dice[0]):
            result += random.randint(1, parsed_dice[1])
        return result

    def __str__(self) -> str:
        return f"{self._dice} - {self._cumulative_dice} - {self._cumulative_damage}"


if __name__ == "__main__":
    d = Dice(description="1d100 plus cumulative 1d20")
    print(f"d1_value: {d.roll()}\n")
    print(f"d1_value: {d.roll()}\n")
    print(f"d1_value: {d.roll()}")
    print(d)

    d = Dice(description="2d100 + 100")
    print(f"\nd2_value: {d.roll()}\n")
    print(d)
