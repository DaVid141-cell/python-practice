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