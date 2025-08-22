## Task 5: Investigate Fare Distribution
# Create a box plot using seaborn to visualize the distribution of passenger fares.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")

# Boxplot of the Titanic dataset of Pclass and fare
sns.boxplot(data=titanic, x='Pclass', y='Fare')
plt.xlabel("Passenger Class")
plt.ylabel("Fare")
plt.title("Fare Distribution by Passenger Class", fontweight='bold')
plt.show()