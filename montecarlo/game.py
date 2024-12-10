class Game:
    """
    A game consisting of rolling multiple similar dice.
    """
    
    def __init__(self, dice):
        """
        Initialize a game with given dice.
        
        Args:
            dice (list): List of Die objects
            
        Raises:
            ValueError: If no dice are provided

        """

        if not dice:
            raise ValueError("At least one die must be provided.")
        self._dice = dice
        self._play_df = None
    
    def play(self, times):
        """
        Play the game by rolling all dice multiple times.
        
        Args:
            times (int): Number of times to roll the dice
        """
        rolls = []
        for roll_num in range(times):
            roll_results = [die.roll(1)[0] for die in self._dice]
            rolls.append(roll_results)
        
        self._play_df = pd.DataFrame(
            rolls, 
            columns=[f'Die_{i}' for i in range(len(self._dice))],
            index=range(times)
        )
    
    def show(self, form='wide'):
        """
        Show results of the most recent play.
        
        Args:
            form (str): 'wide' or 'narrow' format, defaults to 'wide'
        
        Returns:
            pandas.DataFrame: Game results
        
        Raises:
            ValueError: If invalid form is provided
        """
        if form not in ['wide', 'narrow']:
            raise ValueError("Form must be 'wide' or 'narrow'")
        
        if self._play_df is None:
            raise ValueError("No game has been played yet")
        
        if form == 'wide':
            return self._play_df.copy()
        
        # Convert to narrow form
        narrow_df = self._play_df.melt(
            var_name='Die', 
            value_name='Face', 
            ignore_index=False
        ).reset_index()
        narrow_df.set_index(['index', 'Die'], inplace=True)
        return narrow_df

