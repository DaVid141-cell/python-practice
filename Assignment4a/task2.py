## Task 2: Calculate Mean and Median
# Write a NumPy program to calculate the mean and median of the weights in pounds. Print out the results.

import numpy as np

weight_kg = [45.5, 50.2, 55.5, 60.6, 65.2, 70.1, 75.8, 80.1]

np_weight_kg = np.array(weight_kg)
np_weight_lbs = np_weight_kg * 2.2

print("Weights in pounds:", np_weight_lbs)
print("\nMean in pounds:", np.mean(np_weight_lbs))
print("\nMedian in pounds:", np.median(np_weight_lbs))