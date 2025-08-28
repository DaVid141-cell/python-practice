## Activity 5: Time Series Analysis
# Capturing the daily dynamics of COVID-19, assessing the impact of vaccination, and monitoring testing metrics for a comprehensive global overview.
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
covid = pd.read_csv('covid-data.csv')
df = pd.DataFrame(covid)
# 1. Explore the daily trend of new cases and new deaths globally using line plots.
# Group data by date and sum the new cases and new deaths globally
df['date'] = pd.to_datetime(df['date'])
daily_trends = df.groupby('date')[['new_cases', 'new_deaths']].sum().reset_index()
print(daily_trends.head())

# Plot the global daily new cases and deaths
plt.figure(figsize=(12,6))
sns.lineplot(data=daily_trends, x='date', y='new_cases', label='New Cases')
sns.lineplot(data=daily_trends, x='date', y='new_deaths', label='New Deaths')
plt.xlabel('Date')
plt.ylabel('Count')
plt.title('Global Daily New Cases and Deaths')
plt.legend()
plt.show()

# 2. Calculate and visualise the daily average of new cases and deaths globally.
# Group data by date and take the mean across all countries for each day
df['date'] = pd.to_datetime(df['date'])
daily_average = df.groupby('date')[['new_cases', 'new_deaths']].mean().reset_index()
print(daily_average.head())

# Plot the global daily average of new cases and deaths
plt.figure(figsize=(12, 6))
sns.lineplot(data=daily_average, x='date', y='new_cases', label='New Cases')
sns.lineplot(data=daily_average, x='date', y='new_deaths', label='New Deaths')
plt.xlabel('Date')
plt.ylabel('Average per country')
plt.title('Global average New cases and deaths')
plt.legend()
plt.show()

# 3. Explore the trend of vaccination coverage over time globally.
# Group data by date and sum the total number of vaccinated people globally
df['date'] = pd.to_datetime(df['date'])
vaccination = df.groupby('date')['people_vaccinated'].sum().reset_index()

print(vaccination.head())
# Plot vaccination coverage over time
plt.figure(figsize=(12, 6))
sns.lineplot(data=vaccination, x='date', y='people_vaccinated')
plt.xlabel('Date')
plt.ylabel('Total Vaccination')
plt.title('Global coverage of Vaccination')
plt.show()

# 4. Analyze the total tests and positive rate over time globally.
df['date'] = pd.to_datetime(df['date']) # Convert the date into a date and time 
df = df.dropna(subset=['total_tests', 'positive_rate']) # Drop missing values in 'total_tests' and 'positive_rate' before analysis 
total_test = df.groupby('date')['total_tests'].sum().reset_index()# Sum total tests (global total per day)
rate = df.groupby('date')['positive_rate'].mean().reset_index() # Take mean positive rate (average across countries per day)

# Create two y-axes for better visualization by using the twinx()
fig, ax1 = plt.subplots(figsize=(12,6))
# Plot total tests on the first y-axis
sns.lineplot(data=total_test, x='date', y='total_tests', ax=ax1, color="blue", label="Total Tests")
ax1.set_ylabel("Total Tests", color="blue")
# Plot positive rate on the secondary y-axis
ax2 = ax1.twinx()
sns.lineplot(data=rate, x='date', y='positive_rate', ax=ax2, color="red", label="Positive Rate")
ax2.set_ylabel("Positive Rate", color="red")
# added the label for total test
lines, labels = ax1.get_legend_handles_labels()
ax1.legend(lines, labels, loc="upper left")
plt.title("Global Total Tests and Positive Rate Over Time")
plt.show()
