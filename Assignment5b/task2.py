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