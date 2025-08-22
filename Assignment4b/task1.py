## Task 1: Load the Dataset and Explore
# Download the Titanic dataset and assign it to a DataFrame.
# Display the first few rows to get an overview of the data.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Loads the titanic data set
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")

# Display the first few rows of the data set
print("Titanic Rows")
print(titanic.head())
