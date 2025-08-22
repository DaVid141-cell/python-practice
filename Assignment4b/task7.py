## Task 7: Visualize Passenger Class and Age

# Create a scatter plot using matplotlib to show the relationship between passenger age and class.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")

colors = {1: "red", 2: "blue", 3: "green"}

plt.scatter(titanic["Pclass"], titanic["Age"], c=titanic["Pclass"].map(colors), alpha=0.6)
plt.xlabel("Passenger Class")
plt.ylabel("Passenger Age")
plt.title("Visualize Passenger Class and Age", fontweight='bold')
plt.show()