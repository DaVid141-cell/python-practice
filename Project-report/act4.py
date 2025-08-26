## Activity 4 Regional Analysis
# Unvelling regional nuances in COVID-19 dynamics and identifying patterns in case distribution and fatality across time and contients.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

covid = pd.read_csv("covid-data.csv")
df = pd.DataFrame(covid)

# 1. Create a grouped bar chart to visulize new cases by continent and month.
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

group_bar = df.groupby(['continent', 'month'])['new_cases'].sum().reset_index()

sns.barplot(x='month', y='new_cases', hue='continent', data=group_bar)
plt.title("New cases of each continent by month")
plt.xlabel('Months')
plt.ylabel("New cases")
plt.show()

# 2. Visualize the distribution of total COVID-19 cases by year using a box plot.
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

total_covid = df.groupby(['year'])['total_cases'].sum().reset_index()

sns.boxplot(x='year', y='total_cases', hue='year', data=df)
plt.title('Distribution total COVID-19 by year')
plt.xlabel('Year')
plt.ylabel('Total cases')
plt.show()

# 3. Compare total deaths across different continents using bar plot.
compare_deaths = df.groupby(['continent'])['total_deaths'].sum().reset_index()

sns.barplot(x='continent', y='total_deaths', data=compare_deaths)
plt.show()
# 4. Analyze the total cases on a month-by-month basis using bar plot.
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.to_period("M")
monthly_cases = df.groupby('month')['total_cases'].sum().reset_index()
monthly_cases['month'] = monthly_cases['month'].astype(str)

sns.barplot(x='month', y='total_cases', data=monthly_cases, hue='month')
plt.xticks(rotation=90)
plt.title('Total COVID-19 Cases by month')
plt.xlabel('Month')
plt.ylabel('Total Cases')
plt.tight_layout()
plt.show()