IndexError("Face not found in the die.")
        
        # Check if the new weight is numeric
        if not np.isscalar(new_weight):
            raise TypeError("Weight must be a numeric value.")
        
        # Update the weight
        self._die_df.loc[face, 'Weight'] = new_weight

    def roll(self, times=1):
        # Roll the die 'times' number of times
        if times < 1:
            raise ValueError("Number of rolls must be at least 1.")
        
        # Sample from faces based on weights
           outcomes = np.random.choice(self._die_df.index, size=times, p=self._die_df[$
        return outcomes

    def show_state(self):
        # Return a copy of the private die data frame
        return self._die_df.copy()

