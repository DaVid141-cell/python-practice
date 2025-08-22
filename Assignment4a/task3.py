## Task 3: Create 2D Array
# Create a NumPy array np_height_m containing the heights of individuals in meters.
# Combine this array with the weights in pounds np_weight_lbs to create a 2D array np_person_info where each row represents an individual's height and weight.
# Print the resulting 2D array.

import numpy as np

weight_kg = [60.5, 50.2, 80.5, 60.6, 65.2, 70.1, 75.8, 80.1]

np_weight_kg = np.array(weight_kg)
np_height_m = np.array([1.54, 3.60, 1.65, 1.2, 2.75, 1.02, 4.85, 1.90])
np_weight_lbs = np_weight_kg * 2.2

np_person_info = np.column_stack((np_weight_lbs, np_height_m,))

print("Weights and heights of individuals:")
print(np_person_info)
print(f"Array is: {np_person_info.ndim}D",)