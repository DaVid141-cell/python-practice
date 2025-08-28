## Activity 3: Worldwide COVID-19 Overview
# Providing a global and temporal perspective on COVID-19, identifying patterns and correlation crucial for strategic decision-making
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

covid = pd.read_csv("covid-data.csv")
df = pd.DataFrame(covid)
# 1. Visualize the WHO Regions with total COVID-19 cases and total deaths by using bar plots.
who_regions = df.groupby('continent')[['total_cases', 'total_deaths']].sum().reset_index()

#Bar plot for total cases
sns.barplot(x='continent', y='total_cases', data=who_regions)
plt.title('Total number of cases in WHO regions')
plt.xticks(rotation=45)
plt.show()

#Bar plot for total deaths
sns.barplot(x='continent', y='total_deaths', data=who_regions)
plt.title('Total number of deaths in WHO regions')
plt.xticks(rotation=45)
plt.show()

# 2. Explore the world wide monthly trend of COVID-19 cases using a line plot.
# Create a new column 
df['date'] = pd.to_datetime(df['date'])
df['year_month'] = df['date'].dt.to_period('M')
# Create a year and month by grouping them
monthly_trend = df.groupby('year_month')['new_cases'].sum().reset_index()
# Then convert the yearAndMonth to date and time
monthly_trend['year_month'] = monthly_trend['year_month'].astype(str) 

plt.figure(figsize=(12,6))
sns.lineplot(x='year_month', y='new_cases', data=monthly_trend)
plt.title('World Wide Monthly Trend COVID-19')
plt.xticks(rotation=90)
plt.ylabel('New Cases')
plt.xlabel('Month')
plt.show()

# 3. Investigate the correlation between total cases and total deaths using a heatmap.
corr_total = df[['total_cases', 'total_deaths']]

corr = corr_total.corr(numeric_only=True)

#Ploting the heatmap
sns.heatmap(corr, annot=True, linewidths=0.5)
plt.title('HeatMap Correlation of total cases and total deaths')
plt.show()

# 4. Analyze how total cases have evolved over time for a specific locations
s_location = input('Select a location to Analyze: ')

data = df[df['location'] == s_location]   

sns.lineplot(x='date', y='total_cases', data=data)
plt.title(f'Covid-19 Total cases in {s_location} over time')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=90)
plt.show()