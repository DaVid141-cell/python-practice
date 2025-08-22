## Activity 2: Data Cleaning and Feature Engineering
# Enhancing data relevance and structure, enabling focused analysis on key COVID-19 indicators and demographic factors.
import pandas as pd
covid = pd.read_csv("covid-data.csv")
df = pd.DataFrame(covid)
## df['ColumnName'] = df['ColumnName'].fillna(df['ColumnName'].mean())
# First Clean up the dataset that has missing value in columns by doing len(df) * 0.9/90%
valid_values = len(df) * 0.9
df = df.dropna(axis=1, thresh=valid_values) # thresh=valid_values means "keep only columns with at least 90% non-missing values." 


# 1. Impute missing values in the dataset columns.
def categorical_value():
    cloumns_value = df[df['continent'].isna()][['continent', 'iso_code']]
    # Dataset before filling
    print("\nMissing values in column before filling:")
    print(cloumns_value.head(10))

    # Handle missing value categorical data by filling it with data.
    df['continent'] = df['continent'].fillna('No continent found')
    print("\nAfter filling missing values:")
    print(df.loc[cloumns_value.index, ['continent', 'iso_code']])
cat_result = categorical_value() # calls the functions
print(cat_result)

def numerical_value():
    # get a list of the numeric column names
    numeric_columns = df.select_dtypes(include='number').columns.tolist()
    print("Numeric columns:", numeric_columns)

    # Dataset before filling
    nurmeric_value = df[df[numeric_columns].isna()][numeric_columns]
    print("\nMissing values in column before filling:")
    print(nurmeric_value.head(10))

    # Fill missing values with the mean
    df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].median())
    print("\nAfter filling missing values:")
    print(df.loc[:, numeric_columns])
num_result = numerical_value() # calls the functions
print(num_result)

# 2. Remove duplicate rows from the DataFrame.
# by changing the value of the subset into the 'contient' and 'location' we can remove the duplicated rows from them
df_clear = df.drop_duplicates(subset=['continent', 'location'], keep='first', inplace=False)
print("Removed duplicated Rows: ")
print("Rows before:", len(df))
print("Rows after removing duplicates:", len(df_clear))
print(df_clear)

# 3. Create new features if needed (e.g., extract year and month from the 'date' column).
# set 'date' to datetime data type
df['date'] = pd.to_datetime(df['date'])

# Extract year and month into new columns
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

print(df[['date', 'year', 'month']].head())
# 4. Explore unique countries in the dataset and count the total number of countries.
print("\nName of the unique country: ")
print(df['location'].unique())
print("\nNumbers of unique country: ")
print(df['location'].nunique())