##  Question 3: Check if the df DataFrame from the previous question contains any missing values. Print the result.

import pandas as pd

# Create a DataFrame with the specified data
data = {
        'Name': ['John', 'Mary', 'Peter'],
        'Age': [25, 30, 28],
        'Gender': ['Male', 'Female', 'Male']
    }
df = pd.DataFrame(data)

# Check for missing values in the DataFrame
missing_values = df.isnull().any().any()
# Print the result
print("Does the DataFrame contain any missing values?", missing_values)
