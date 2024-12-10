class Analyzer:
    """
    Analyze the results of a game, providing statistical insights.
    """
    
    def __init__(self, game):
        """
        Initialize analyzer with a game.
        
        Args:
            game (Game): Game object to analyze
        
        Raises:
            ValueError: If input is not a Game object
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object")
        
        self._game = game
        self._play_results = game.show()
    
    def jackpot(self):
        """
        Count number of rolls where all dice show the same face.
        
        Returns:
            int: Number of jackpots
        """
        return ((self._play_results.apply(lambda x: len(set(x)) == 1, axis=1)).sum())
    
    def face_counts_per_roll(self):
        """
        Count occurrences of each face in each roll.
        
        Returns:
            pandas.DataFrame: Face counts per roll
        """
        unique_faces = set(self._play_results.values.ravel())
        counts_df = pd.DataFrame(index=self._play_results.index)
        
        for face in unique_faces:
            counts_df[face] = (self._play_results == face).sum(axis=1)
        
        return counts_df
    
    def combo(self):
        """
        Count distinct combinations of faces rolled.
        
        Returns:
            pandas.DataFrame: Combination counts
        """
        combos = [tuple(sorted(roll)) for roll in self._play_results.values]
        combo_counts = pd.Series(combos).value_counts()
        return pd.DataFrame(combo_counts).rename(columns={0: 'count'})
    
    def permutation(self):
        """
        Count distinct permutations of faces rolled.
        
        Returns:
            pandas.DataFrame: Permutation counts
        """
        perms = [tuple(roll) for roll in self._play_results.values]
        perm_counts = pd.Series(perms).value_counts()
        return pd.DataFrame(perm_counts).rename(columns={0: 'count'})
