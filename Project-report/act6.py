## Activity 6: In-Depth Country Analysis
# Conducting an in-depth examination of specific countries, understanding the correlation between cases and deaths globally, and exploring continental variations in case distribution.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
covid = pd.read_csv('covid-data.csv')
df = pd.DataFrame(covid)

# 1. Visualize a specific country’s total COVID-19 cases and deaths over time.
df['date'] = pd.to_datetime(df['date'])
country = input('Select a country to check: ')
country_df = df[df['location'] == country]
total = country_df.groupby('date')[['total_cases', 'total_deaths']].sum().reset_index()

# Creating two different y-axes with thier scale
fig, ax1 = plt.subplots(figsize=(12, 6))
#plot on ax1 as total cases
p1, = ax1.plot(total['date'], total['total_cases'], color='green', label='Total Cases')
ax1.set_ylabel('Total Cases', color='green')
#plot on ax2 as total deaths
ax2 = ax1.twinx()
p2, = ax2.plot(total['date'], total['total_deaths'], color='red', label='Total Deaths')
ax2.set_ylabel('Total Deaths', color='red')
# Combine both lines for the legend
lines = [p1, p2]
labels = [line.get_label() for line in lines]
ax1.legend(lines, labels, loc='upper left')

plt.title(f"COVID-19 Total Cases and Deaths in {country}")
plt.show()

# 2. Get user input for the country and metric (total_cases or total_deaths), and plot a line chart for the user-selected values.
#Takes user inputs
country = input("Select a Country: ")
metric = input("Choose a metric (total_cases/total_deaths): ")

country_df = df[df['location'] == country] # takes the user input and store's in a variable
#ploting
plt.figure(figsize=(12, 6))
plt.plot(country_df['date'], country_df[metric], label=metric.capitalize(), color='red')
plt.xlabel("Date")
plt.ylabel(metric.replace("_", " ").capitalize())
plt.title(f"{metric.replace('_', ' ').capitalize()} over time in {country}")
plt.legend()
plt.xticks(rotation=45)
plt.show()

# 3. Analyze the distribution of total cases across different continents using a box plot.
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='continent', y='total_cases')
plt.title("Distribution of Total COVID-19 Cases Across Continents")
plt.ylabel("Total Cases")
plt.xlabel("Continent")
plt.yscale('log') # using the yscale to make the visualization better
plt.show()

# 4. Visualize the year-wise monthly trend of new COVID-19 cases for the user’s selected country.
country = input("Enter a country for monthly trend: ") # takes the user selected country
country_df = df[df['location'] == country].copy()

# Extract the date into year and month
country_df['year'] = country_df['date'].dt.year
country_df['month'] = country_df['date'].dt.month

# Group by year & month to sum all the total cases
monthly_trend = country_df.groupby(['year','month'])['new_cases'].sum().reset_index()
# Created a proper 'date' column representing the first day of each month
monthly_trend['date'] = pd.to_datetime(monthly_trend['year'].astype(str) + '-' + monthly_trend['month'].astype(str) + '-01')

# Plot the lineplot of the new cases
plt.figure(figsize=(12,6))
sns.lineplot(data=monthly_trend, x="date", y="new_cases", marker="o")
plt.title(f"Monthly Trend of New COVID-19 Cases in {country}")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.show()