## Task 6: Correlation Between Variables
# Generate a heatmap using seaborn to visualize the correlation matrix of the numerical variables in the dataset.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")

corr = titanic.corr(numeric_only=True)

# Plot Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr, annot=True, linewidths=0.5)
plt.title("Correlation Heatmap of Titanic Numerical Variables", fontweight='bold')
plt.show()