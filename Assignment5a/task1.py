## Question 1: Create a Pandas Series called s with the following values: [1, 3, 5, np.nan, 6, 8]. Print the series.
import numpy as np
import pandas as pd

# Create a Pandas Series with the specified values
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# Print the series
print("Series s:")
print(s)