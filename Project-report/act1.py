## Activity 1: Data Loading and Exploration	

# Initializing the analysis by loading and exploring the dataset, ensuring data integrity and format consistency for accurate downstream analysis. 
import pandas as pd

# 1. Load the COVID-19 DataFrame using pandas from the provided dataset files. 
covid = pd.read_csv("covid-data.csv")

# 2. Display the first 5 and last 5 rows of the DataFrame. 
df = pd.DataFrame(covid)
first_row = df.head(5)
last_row = df.tail(5)
print("First row of the data: ")
print(first_row)
print("\nLast row of the data: ")
print(last_row)

# 3. Check for missing values in the dataset and decide on a strategy to handle them. 
missing_value = df.isna().sum()
print("Missing Value of the dataset: ")
print(missing_value)

# 4. Remove the columns with more than 90% of missing values.
valid_values = len(df) * 0.9
df = df.dropna(axis=1, thresh=valid_values) # thresh=valid_values means "keep only columns with at least 90% non-missing values."
print("\nRemove columns before and after: ")
print("Shape after cleaning:", df.shape)
print("\nRemaining columns:", df.columns)  

# 5. Convert the 'date' column to the datetime data type. 
print("\nDate types before: ")
print(df['date'].dtype)
df['date'] = pd.to_datetime(df['date'], errors='coerce')
print("\nDate types now: ")
print(df['date'].dtype)
