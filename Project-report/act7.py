## Activity 7: Additional Insights
# Extracting additional insights, examining the influence of external factors, and evaluating regional disparities for a holistic understanding of the COVID-19 landscape.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data set
covid = pd.read_csv('covid-data.csv')
df = pd.DataFrame(covid)

# 1. Visualize the fatality rate (total_deaths / total_cases) over time globally.
df['date'] = pd.to_datetime(df['date'])
df = df.dropna(subset=['total_cases']) # drops the none values in the row
total_fatality_rate = df.groupby('date')[['total_deaths', 'total_cases']].sum().reset_index()
# Divided the total deaths and cases to get the rate and then times it 100 to make it percentage data
total_fatality_rate['fatality_rate'] = (total_fatality_rate['total_deaths'] / total_fatality_rate['total_cases']) * 100 

plt.figure(figsize=(12, 6))
sns.lineplot(data=total_fatality_rate, x='date', y='fatality_rate')
plt.title("Global COVID-19 Fatality Rate Over Time")
plt.ylabel("Fatality Rate by %")
plt.xlabel("Date")
plt.show()

# 2. Explore the positivity rate (total_cases / total_tests) versus total tests conducted, using the x-axis as a logarithmic scale for better visualization.
df = df[df['total_tests'] > 0]
df['positive_rate'] = (df['total_cases'] / df['total_tests'])

plt.figure(figsize=(12, 6))
plt.scatter(df['total_tests'], df['positive_rate'], alpha=0.5)
plt.xscale("log")
plt.title("Positivity Rate vs Total Tests Conducted")
plt.xlabel('Total Test Conducted')
plt.ylabel('Positive Rate')
plt.show()

# 3. Analyze the fatality rate and its relationship with smoking (use male_smokers and female_smokers columns).
df = df.dropna(subset=['female_smokers', 'male_smokers'])
fatality_rate = df.groupby('location')[['total_deaths', 'total_cases', 'female_smokers', 'male_smokers']].max().reset_index()
# Divided the total deaths and cases to get the rate and then times it 100 to make it percentage data
fatality_rate['fatality_rate'] = (fatality_rate['total_deaths'] / fatality_rate['total_cases']) * 100

plt.figure(figsize=(12,6))
sns.scatterplot(data=fatality_rate, x='male_smokers', y='fatality_rate', label='Male Smokers', color='black')
sns.scatterplot(data=fatality_rate, x='female_smokers', y='fatality_rate', label='Female Smokers', color='pink')
plt.title("Fatality Rate vs Smoking Rates (Male & Female)")
plt.xlabel("Smokers (%)")
plt.ylabel("Fatality Rate (%)")
plt.legend()
plt.show()

# 4. Create a heatmap to analyze the relationship between hospital beds per thousand and fatality rate.
fatality_rate = df.groupby('location')[['total_deaths', 'total_cases', 'hospital_beds_per_thousand']].max().reset_index()
# Divided the total deaths and cases to get the rate and then times it 100 to make it percentage data
fatality_rate['fatality_rate'] = (fatality_rate['total_deaths'] / fatality_rate['total_cases']) * 100
corr_total = fatality_rate[['fatality_rate', 'hospital_beds_per_thousand']]

corr = corr_total.corr(numeric_only=True) # calculate the fatality rate with hospital beds by correlation

plt.figure(figsize=(12, 6))
sns.heatmap(corr, annot=True, linewidths=0.5)
plt.title('Heatmap')
plt.show()