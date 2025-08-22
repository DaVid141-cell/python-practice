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
