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

## Task 2: Visualize Passenger Survival
# Create a bar plot using seaborn to visualize the count of survivors and non-survivors.

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

## Task 3: Analyze Passenger Age Distribution
# Create a histogram using matplotlib to show the distribution of passenger ages.

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")

# Extract the column of the Titanic Age and remove the Nan data by the .dropna()
ages = titanic['Age'].dropna()

# convert the numpy array and sort to lowest to highest
def numpy_age():
    ages_np = np.array(ages)
    ages_sort = np.sort(ages_np)

    return ages_sort

# Prints the sorted ages
result_sort = numpy_age()
print(result_sort)

plt.hist([result_sort[result_sort<18], result_sort[result_sort>=18]],
         bins=20, histtype='bar', color=['green','red'], 
         label=['Under 18','18 and above'])

plt.legend()
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.title("Passengers Age range from Lowest to highest", fontweight='bold')
plt.show()

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