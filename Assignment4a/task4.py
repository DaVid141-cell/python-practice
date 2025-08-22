## Task 4: Calculate BMI
# Write a function that takes the 2D array np_person_info created in Task 3 as input.
# Calculate the Body Mass Index (BMI) for each individual as bmi_array. BMI is calculated using the formula: BMI = weight (kg) / (height (m) ** 2).
# Print the BMI values for each individual.

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
print("Weights and heights of individuals:")
print(np_person_info)
print("\nBMI values for each individual:")
print(bmi_values)


