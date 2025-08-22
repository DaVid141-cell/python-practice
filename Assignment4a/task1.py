## Task 1: Convert Weights to Pounds

# Create a Python list weight_kg with weight values
# Convert weight_kg to numpy array np_weight_kg
# Convert np_weight_kg to weight in Pounds np_weight_lbs
# Hint: Use the conversion factor of 2.2 pounds per kilogram

import numpy as np

weight_kg = [45.5, 50.2, 55.5, 60.6, 65.2, 70.1, 75.8, 80.1]

np_weight_kg = np.array(weight_kg)
np_weight_lbs = np_weight_kg * 2.2

# Print the converted weights
print("Weights in Kilograms:", np_weight_kg)
print("Weights in Pounds:", np_weight_lbs)




