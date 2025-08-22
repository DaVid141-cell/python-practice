## Task 4: Descriptive Statistics:

import pandas as pd

# Titanic Dataset
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")
df = pd.DataFrame(titanic)

# Generate descriptive statistics for the numerical columns using the describe() method.
print(df.describe())

