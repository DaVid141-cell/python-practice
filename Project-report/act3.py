import pandas as pd
covid = pd.read_csv("covid-data.csv")
df = pd.DataFrame(covid)

print(df.describe())