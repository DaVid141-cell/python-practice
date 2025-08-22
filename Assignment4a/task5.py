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


