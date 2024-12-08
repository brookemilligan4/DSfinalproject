import numpy as np
import pandas as pd
import random

class Die:
    def __init__(self, faces):
        # Check if faces is a NumPy array
        if not isinstance(faces, np.ndarry):
            raise TypeError("Faces must be a Numpy array.")
        # Check if faces contain distinct values
        if len(faces) != len(np.unique(faces)):
            raise ValueError("Faces must contain distinct values.")
        # Initialize faces and weights
        self._faces = faces
        self._weights = np.ones(len(faces))
        #Default weights to 1 for each face
        self._die_df = pd.DataFrame({'Face': faces, 'Weight': self._weights}).set_index('Face')
    def change_weight(self, face, new_weight):
        # Check if the face is valid
        if face not in self._die_df.index:
            raise IndexError("Face not found in the die.")
        # Check if the new weight is numeric
        assert isinstance(new_weight, (int, float)), "Weight must be a numeric value."
        # Update the weight
        self._die_df.loc[face, 'Weight'] = new_weight
    def roll(self, times=1):
        # Roll the die 'times' number of times
        if times < 1:
            raise ValueError("Number of rolls must be at least 1.")
        # Sample from faces based on weights
        outcomes = np.random.choice(self._die_df.index, size=times, p=self._die_df['Weight'] / self._die_df['Weight'].sum())
    def show_state(self):
        # Return a copy of the private die data frame
        return self._die_df.copy()
