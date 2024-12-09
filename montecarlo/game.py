import random
import pandas as pd

class Die:
    def __init__(self, faces):
        if faces < 1:
            raise ValueError("Die must have at least one face.")
        self.faces = faces

    def roll(self):
        return random.randint(1, self.faces)

class Game:
    def __init__(self, dice):
        if not isinstance(dice, list) or len(dice) < 2:
            raise ValueError("Dice must be a list with at least two Die objects.")  # Change TypeError to ValueError
        if len(set(die.faces for die in dice)) != 1:
            raise ValueError("All dice must have the same number of faces.")
        self.dice = dice
        self.results = []

    def play(self, rolls):
        if rolls < 1:
            raise ValueError("Rolls must be at least 1.")
        self.results = []
        for _ in range(rolls):
            roll_result = [die.roll() for die in self.dice]  # Correctly call roll() without additional arguments
            self.results.append(roll_result)

    def show_results(self):
        return pd.DataFrame(self.results, columns=[f'Die {i+1}' for i in range(len(self.dice))])

    def get_results(self, form):
        if form == 'wide':
            return self.show_results()
        elif form == 'narrow':
            narrow_df = self.show_results().melt(var_name='Die', value_name='Outcome')
            return narrow_df
        else:
            raise ValueError("Invalid form. Use 'wide' or 'narrow'.")

