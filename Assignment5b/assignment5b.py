## Task 1: Loading the Data:

import pandas as pd

# Dataset: Titanic Dataset
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")
# Load the Titanic dataset into a Pandas DataFrame. 
df = pd.DataFrame(titanic)
print(df)

## Task 2: Initial Exploration:

import pandas as pd

# Titanic Dataset loads
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")
# Display the first 5 rows of the dataset to get an overview.
df = pd.DataFrame(titanic)
print(df.head(5))

# Provide basic information about the dataset using the info() method.
print()
# Display detailed info about the dataset including column names, non-null counts, and data types
print(df.info(verbose=True))
print()
# Display only a summary with column count and dtypes, without showing all column details
print(df.info(verbose=False))

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

## Task 4: Descriptive Statistics:

import pandas as pd

# Titanic Dataset
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")
df = pd.DataFrame(titanic)

# Generate descriptive statistics for the numerical columns using the describe() method.
print(df.describe())

## Task 5: Unique Values:

import pandas as pd

# Titanic Dataset and Dataframe load out
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")
df = pd.DataFrame(titanic)

# List unique values in the 'Pclass' column.
print("Unique Values of the Pclass:")
print(df['Pclass'].unique())
# Count the occurrences of each unique value in the 'Embarked' column.
print("\nUnique Values counts of each Embarked:")
print(df['Embarked'].value_counts())

## Task 6: Data Manipulation:

import pandas as pd

# Titanic Dataset and dataframe load out
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")
df = pd.DataFrame(titanic)

# Create a new column named 'FamilySize' that represents the sum of 'SibSp' and 'Parch'.
df['FamilySize'] = df['SibSp'] + df['Parch']
print("New Dataframe column: ")
print(df)

# Drop the 'Cabin' column from the dataset.
df = df.drop(columns='Cabin')
print("\nDrop column: ")
print(df)

## Task 7: Filtering and Sorting:
import pandas as pd

# Titanic Dataset and dataframe load out
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")
df = pd.DataFrame(titanic)

# Create a new DataFrame containing only passengers with an age greater than 30.
df['filter_age'] = df['Age'].where(df['Age'] > 30)
# Drop rows where 'filter_age' is NaN
filtered_df = df.dropna(subset=['filter_age'])
print(filtered_df.head())

# Sort the DataFrame by 'Fare' in descending order.
df = df.sort_values(by='Fare', ascending=False)
print("\nSorted Dataframe 'Fare': ")
print(df)

## Task 8: Data Analysis:
import pandas as pd
import matplotlib.pyplot as plt

# Titanic Dataset and dataframe load out
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")
df = pd.DataFrame(titanic)

# Calculate the survival rate for different passenger classes ('Pclass').
print("Percentage of the survival rate in Pclass: ")
survival_rate = df.groupby('Pclass')['Survived'].mean() * 100
print(survival_rate) # with * 100 this will return the survival rate as a percentage instead of a decimal  

# Identify and display the passenger with the highest 'Fare'.
print("\nPassenger with the highest Fare: ")
print(df.loc[df['Fare'].idxmax()])

# Plot as a bar chart (better for categorical comparison)
survival_rate.plot(kind='barh', color='skyblue', edgecolor='black')
plt.title("Survival Rate by Passenger Class", fontweight='bold')
plt.ylabel("Passenger Class")
plt.xlabel("Survival Rate (%)")
plt.show()

## Conclusion:
#Throughout these tasks, I learned step by step how to work with data using Python and pandas. At first, I was only practicing basic things like creating DataFrames, checking data types, and describing datasets, but later I got more confident in filtering, sorting, and grouping data. I also learned how to calculate meaningful insights, like survival rates, and how to identify important details such as the passenger who paid the highest fare. Using matplotlib helped me visualize the results, which made the analysis clearer and more interesting. Overall, this experience taught me not only the technical skills of data analysis but also how to think critically and interpret the results in a meaningful way.