## Task 8: Data Analysis:
import pandas as pd
import matplotlib.pyplot as plt

# Titanic Dataset and dataframe load out
titanic = pd.read_csv("asset-v1_EDUCLaaS+PYD+PDDS-PYD-0824-27Nov2024+type@asset+block@titanic.csv")
df = pd.DataFrame(titanic)

# Calculate the survival rate for different passenger classes ('Pclass').
print("Percentage of the survival rate in Pclass: ")
survival_rate = df.groupby('Pclass')['Survived'].mean() * 100
print(survival_rate) # with * 100 this will return the survival rate as a percentage instead of a decimal  

# Identify and display the passenger with the highest 'Fare'.
print("\nPassenger with the highest Fare: ")
print(df.loc[df['Fare'].idxmax()])

# Plot as a bar chart (better for categorical comparison)
survival_rate.plot(kind='barh', color='skyblue', edgecolor='black')
plt.title("Survival Rate by Passenger Class", fontweight='bold')
plt.ylabel("Passenger Class")
plt.xlabel("Survival Rate (%)")
plt.show()

