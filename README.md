# DSfinalproject
Project Name: Final Porject

Author: Brooke Milligan

Version: 1.0.0

License: MIT License

Description: Final project for DS 5100

import numpy as np
from dice_module import Die

faces = np.array([1, 2, 3, 4, 5, 6])
die = Die(faces)
roll_result = die.roll()  # Assuming you have a roll method

from dice_module import Game

dice = [Die(faces), Die(faces), Die(faces)]
game = Game(dice)
game.play(5)  # Roll the dice 5 times

from dice_module import Analyzer

analyzer = Analyzer(game)
### API
This section lists all classes and their methods.

#### Class: Die
- **Constructor**: `Die(faces: np.ndarray)`
  - Initializes a Die object with a specified set of faces.
  - Raises `TypeError` if `faces` is not a NumPy array.
  - Raises `ValueError` if `faces` does not contain distinct values.

- **Method**: `roll()`
  - (Assumed) Returns a random face from the die.

#### Class: Game
- **Constructor**: `Game(dice: list)`
  - Initializes a Game object with a list of Die objects.
  - Raises `ValueError` if `dice` is not a list of at least two Die objects or if the dice do not have the same number of faces.

- **Method**: `play(rolls: int)`
  - Rolls the dice a specified number of times.

- **Method**: `show_results()`
  - (Assumed) Returns the results of the dice rolls conducted during the game.

#### Class: Analyzer
- **Constructor**: `Analyzer(game: Game)`
  - Initializes an Analyzer object with a Game object.
  - Raises `ValueError` if the provided `game` parameter is not an instance of the Game class.

- **Method**: (Detail further methods as needed)
  - (Assumed) Analyze the results stored in `self.results`.

#### Class: TestAnalyzer
- **Method**: `setUp()`
  - Prepares the test environment by creating Die and Game objects and invoking the play method.

- **Method**: `test_initialization_with_invalid_game()`
  - Tests the initialization of the Analyzer with an invalid input, ensuring a `ValueError` is raised.
