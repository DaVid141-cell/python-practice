## Task 3: Handling Missing Values:

import pandas as pd
 
# Titanic Dataset
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")

df = pd.DataFrame(titanic)
# Identify and count the number of missing values in each column.
# isna() will show the messing values by true or false with the .sum() it will only show the numbers of missing value.
titanic_missing_value = df.isna().sum()
print(titanic_missing_value)

# Decide on an appropriate strategy for handling missing values in at least two columns and implement it.

# Function to handle missing values
def handle_missing(column_name):
    # Show rows with missing values in the chosen column
    selected_columns = df[df[column_name].isna()][[column_name, "Name"]]
    
    # Show before filling
    print("\nMissing values in column before filling:")
    print(selected_columns.head(20))  

    # Ask for replacement
    missing_value = input(f"Enter a value to replace missing data in '{column_name}': ")

    # Fill missing values with the user-provided value
    df[column_name] = df[column_name].fillna(missing_value)

    # Show after filling
    print("\nAfter filling missing values:")
    print(df.loc[selected_columns.index, [column_name, "Name"]].head(20))

# User input
column_name = input("\nSelect a column to check: ")

# Call the function
handle_missing(column_name)