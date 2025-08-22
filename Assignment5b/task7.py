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