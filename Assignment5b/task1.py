## Task 1: Loading the Data:

import pandas as pd


# Dataset: Titanic Dataset
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")

# Load the Titanic dataset into a Pandas DataFrame. 

df = pd.DataFrame(titanic)

print(df)