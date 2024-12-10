import numpy as np
import pandas as pd
import random

class Die:
    """
    A class representing a die with N sides and associated weights.
    
    A die can be fair (equal weights) or biased (unequal weights).
    Supports rolling and weight modification.
    """
    
    def __init__(self, faces):
        """
        Initialize a die with given faces.
        
        Args:
            faces (numpy.ndarray): Array of unique faces for the die
        
        Raises:
            TypeError: If faces is not a NumPy array
            ValueError: If faces contain duplicate values
        """
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array")
        
        if len(set(faces)) != len(faces):
            raise ValueError("Faces must be unique")
        
        self._faces = faces
        self._weights = np.ones(len(faces), dtype=float)
        self._die_df = pd.DataFrame({'faces': faces, 'weights': self._weights}, index=faces)
    
    def change_weight(self, face, new_weight):
        """
        Change the weight of a specific face.
        
        Args:
            face: Face to change weight for
            new_weight (numeric): New weight value
        
        Raises:
            IndexError: If face is not in die
            TypeError: If weight is not numeric
        """
        if face not in self._faces:
            raise IndexError("Face not in die")
        
        try:
            new_weight = float(new_weight)
        except (TypeError, ValueError):
            raise TypeError("Weight must be numeric")
        
        self._die_df.loc[face, 'weights'] = new_weight
    
    def roll(self, times=1):
        """
        Roll the die multiple times.
        
        Args:
            times (int): Number of rolls, defaults to 1
        
        Returns:
            list: Outcomes of the rolls
        """
        return list(np.random.choice(
            self._faces, 
            size=times, 
            p=self._die_df['weights']/self._die_df['weights'].sum()
        ))
    
    def show(self):
        """
        Show current state of the die.
        
        Returns:
            pandas.DataFrame: Copy of die's data frame
        """
        return self._die_df.copy()
