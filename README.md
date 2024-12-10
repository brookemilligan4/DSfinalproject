# DSfinalproject
Project Name: Final Porject

Author: Brooke Milligan

Version: 1.0.0

License: MIT License

Description: Final project for DS 5100

 Synopsis
This project includes the following classes:

1. Die: Represents a single die with customizable faces and weights.
2. Game: Manages multiple dice and facilitates gameplay.
3. Analyzer: Analyzes the results of the game, providing insights such as jackpots, face counts, combinations, and permutations.

 API

 Classes

-Die
  -Methods:
    - __init__(faces: np.ndarray): Initializes the die with specified faces.
    - change_weight(face: int, weight: float): Changes the weight of a specific face.
    - show(): Displays the current faces and their weights.
    - roll(n: int): Rolls the die n times and returns the results.

-Game
  - Methods:
    - __init__(dice: List[Die]): Initializes the game with a list of dice.
    - play(n: int): Plays the game for n rounds.
    - show(format: str = 'wide'): Displays the results of the game in specified format (wide/narrow).

- Analyzer
  - Methods:
    - __init__(game: Game): Initializes the analyzer with a game instance.
    - jackpot(): Returns the total number of jackpots.
    - face_counts_per_roll(): Returns a DataFrame with face counts for each roll.
    - combo(): Returns a DataFrame of combinations rolled.
    - permutation(): Returns a DataFrame of permutations rolled.   
