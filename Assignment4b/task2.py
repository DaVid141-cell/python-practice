## Task 2: Visualize Passenger Survival
## Create a bar plot using seaborn to visualize the count of survivors and non-survivors.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")

# Shows the Barplot of the numbers of survivors
sns.countplot(x='Survived', data=titanic, hue='Sex')

# Lables of the barplots
plt.ylabel("Count")
plt.title('Titanic Survivors and non-survivors', fontweight='bold')
plt.show()