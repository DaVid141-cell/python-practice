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