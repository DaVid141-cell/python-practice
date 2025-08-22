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

## Task 2: Calculate Mean and Median
# Write a NumPy program to calculate the mean and median of the weights in pounds. Print out the results.

import numpy as np

weight_kg = [45.5, 50.2, 55.5, 60.6, 65.2, 70.1, 75.8, 80.1]

np_weight_kg = np.array(weight_kg)
np_weight_lbs = np_weight_kg * 2.2

print("Weights in pounds:", np_weight_lbs)
print("\nMean in pounds:", np.mean(np_weight_lbs))
print("\nMedian in pounds:", np.median(np_weight_lbs))

## Task 3: Create 2D Array
# Create a NumPy array np_height_m containing the heights of individuals in meters.
# Combine this array with the weights in pounds np_weight_lbs to create a 2D array np_person_info where each row represents an individual's height and weight.
# Print the resulting 2D array.

import numpy as np

weight_kg = [45.5, 50.2, 55.5, 60.6, 65.2, 70.1, 75.8, 80.1]

np_weight_kg = np.array(weight_kg)
np_height_m = np.array([1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90])
np_weight_lbs = np_weight_kg * 2.2

np_person_info = np.column_stack((np_weight_lbs, np_height_m,))

print("Weights and heights of individuals:")
print(np_person_info)
print(f"Array is: {np_person_info.ndim}D",)

## Task 4: Calculate BMI
# Write a function that takes the 2D array np_person_info created in Task 3 as input.
# Calculate the Body Mass Index (BMI) for each individual as bmi_array. BMI is calculated using the formula: BMI = weight (kg) / (height (m) ** 2).
# Print the BMI values for each individual.

import numpy as np

weight_kg = [45.5, 50.2, 55.5, 60.6, 65.2, 70.1, 75.8, 80.1]

np_weight_kg = np.array(weight_kg)
np_height_m = np.array([1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90])
np_weight_lbs = np_weight_kg * 2.2

np_person_info = np.column_stack((np_weight_lbs, np_height_m,))

def calculate_bmi(person_info):
    # Extract weights in kg and heights in m from the 2D array
    weights_kg = person_info[:, 0] / 2.2  # Convert pounds to kg
    heights_m = person_info[:, 1]
    
    # Calculate BMI
    bmi_array = (weights_kg / (heights_m ** 2))
    return bmi_array

# Calculate BMI for each individual
bmi_values = calculate_bmi(np_person_info)
print("Weights and heights of individuals:")
print(np_person_info)
print("\nBMI values for each individual:")
print(bmi_values)

## Task 5: Filter Individuals by BMI
# Write a NumPy program to append bmi_array to np_person_info 
# Filter individuals from the resulting array who have a BMI greater than 25.
# Print the filtered results.

import numpy as np

weight_kg = [60.5, 50.2, 80.5, 60.6, 65.2, 70.1, 75.8, 80.1]

np_weight_kg = np.array(weight_kg)
np_height_m = np.array([1.54, 3.60, 1.65, 1.2, 2.75, 1.02, 4.85, 1.90])
np_weight_lbs = np_weight_kg * 2.2

np_person_info = np.column_stack((np_weight_lbs, np_height_m,))

def calculate_bmi(person_info):
    # Extract weights in kg and heights in m from the 2D array
    weights_kg = person_info[:, 0] / 2.2  # Convert pounds to kg
    heights_m = person_info[:, 1]
    
    # Calculate BMI
    bmi_array = (weights_kg / (heights_m ** 2))
    return bmi_array

# Calculate BMI for each individual
bmi_values = calculate_bmi(np_person_info)

# Append the BMI values into the 2D array in person_info
np_person_info_bmi = np.column_stack((np_person_info, bmi_values))

# Filtered the results that is greater than 25
filerted_results = np_person_info_bmi[bmi_values > 25]

print("\nBMI values for each individual:")
print(bmi_values)
print("Filtered Results: (w/h/bmi)")
print(filerted_results)