## Task 4: Explore Class-wise Distribution
# Use seaborn to create a count plot to display the number of passengers in each class.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")

# Count plot of passengers per class
sns.countplot(x='Pclass', data=titanic, hue='Pclass')
plt.xlabel('Pclass')
plt.ylabel("Passengers")
plt.title('Titanic Passegers Classes', fontweight='bold')
plt.show()