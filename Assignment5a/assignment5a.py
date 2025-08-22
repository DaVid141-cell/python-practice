## Question 1: Create a Pandas Series called s with the following values: [1, 3, 5, np.nan, 6, 8]. Print the series.

import numpy as np
import pandas as pd

# Create a Pandas Series with the specified values
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# Print the series
print("Series s:")
print(s)

## Question 2: Create a DataFrame called df with the following data:
#     Name  Age  Gender
# 0   John   25    Male
# 1   Mary   30  Female
# 2  Peter   28    Male

import pandas as pd

# Create a DataFrame with the specified data
data = {
        'Name': ['John', 'Mary', 'Peter'],
        'Age': [25, 30, 28],
        'Gender': ['Male', 'Female', 'Male']
    }

df = pd.DataFrame(data)
print("DataFrame df:")
print(df)

##  Question 3: Check if the df DataFrame from the previous question contains any missing values. Print the result.

import pandas as pd

# Create a DataFrame with the specified data
data = {
        'Name': ['John', 'Mary', 'Peter'],
        'Age': [25, 30, 28],
        'Gender': ['Male', 'Female', 'Male']
    }
df = pd.DataFrame(data)

# Check for missing values in the DataFrame
missing_values = df.isnull().any().any()
# Print the result
print("Does the DataFrame contain any missing values?", missing_values)

## Question 4: Merge the following two DataFrames, df1 and df2, on the 'ID' column:
# df1:
#    ID  Name
# 0   1  John
# 1   2  Mary
# df2:
#    ID  Age
# 0   1   25
# 1   2   30

import pandas as pd

# Create the first DataFrame
df1 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['John', 'Mary']
})
# Create the second DataFrame
df2 = pd.DataFrame({
    'ID': [1, 2],
    'Age': [25, 30]
})

# Merge the two DataFrames on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID')
# Print the merged DataFrame
print("Merged DataFrame:")
print(merged_df)

## Question 5: Concatenate the following two DataFrames, df3 and df4, vertically:
# df3:
#    ID  Name
# 0   1  John
# 1   2  Mary
# df4:
#    ID  Age
# 0   3   28
# 1   4   32

import pandas as pd

df3 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['John', 'Mary']
})  
df4 = pd.DataFrame({
    'ID': [3, 4],
    'Age': [28, 32]
})

# Concatenate the two DataFrames vertically
concatenated_df = pd.concat([df3, df4], ignore_index=True)
# Print the concatenated DataFrame
print("Concatenated DataFrame:")
print(concatenated_df)

## Question 6: Create a DataFrame called df5 with the following data:
#    Name  Age
# 0  John   25
# 1  Mary   30
# 2  Alan   35
# Set the 'Name' column as the index of the DataFrame. Print the DataFrame.

import pandas as pd

df5 = pd.DataFrame({
    'Name': ['John', 'Mary', 'Alan'],
    'Age': [25, 30, 35]
})

# Set the 'Name' column as the index of the DataFrame
df5.set_index('Name', inplace=True)
# Print the DataFrame
print("DataFrame df5 with 'Name' as index:")
print(df5)

## Question 7: Concatenate the following two DataFrames, df6 and df7, horizontally:
# df6:
#   ID  Score
# 0   1     85
# 1   2     92
# df7:
#    ID  Grade
# 0   1     A
# 1   2     B
# Print the concatenated DataFrame

import pandas as pd

df6 = pd.DataFrame({
    'ID': ['1', '2'],
    'Score': ['85', 92] 
})
df7 = pd.DataFrame({
    'ID': ['1', '2'],
    'Grade': ['A', 'B']
})

concat = pd.concat([df6, df7], axis=1 )
print("Concatenated DataFrame:")
print(concat)

## Question 8: Append the following DataFrame, df8, to the df9 DataFrame:
# df8:
#    ID  Name
# 0   3  Alan
# 1   4   Zoe
# df9:
#    ID   Name
#0   1   John
# 1   2   Mary

import pandas as pd

# Create the first DataFrame df8
df8 = pd.DataFrame({
    'ID': [3, 4],
    'Name': ['Alan', 'Zoe']
})
# Create the second DataFrame df9
df9 = pd.DataFrame({
    'ID': [1, 2],
    'Name': ['John', 'Mary']
})

# Append df8 to df9 using pd.concat
df9 = pd.concat([df9, df8], ignore_index=True)
# Print the resulting DataFrame
print("DataFrame df9 after appending df8:")
print(df9)

## Question 9: Given the following DataFrame, df10:
#    Name  Age  Gender
# 0  John   25    Male
# 1  Mary   30  Female
# 2  Alan   35    Male
# 3  Zoe    28  Female
# 4  Mark   32    Male
# Print the first three rows of the DataFrame.

import pandas as pd

# Create the DataFrame df10
df10 = pd.DataFrame({
    'Name': ['John', 'Mary', 'Alan', 'Zoe', 'Mark'],
    'Age': [25, 30, 35, 28, 32],
    'Gender': ['Male', 'Female','Male', 'Female','Male']
})

# Print the first three rows of the DataFrame
print("First three rows of DataFrame df10:")
print(df10.head(3))

## Question 10: Given the DataFrame df11:
#    ID  Name
# 0   1  John
# 1   2  Mary
# 2   3  Alan
# 3   4  Zoe
# 4   5  Mark
# Select and print the row with the ID value of 3.

import pandas as pd

# Create the DataFrame df11
df11 = pd.DataFrame({
    'ID': [1, 2, 3, 4, 5],
    'Name': ['John', 'Mary', 'Alan', 'Zoe', 'Mark']
})

# Select the row with ID value of 3
num = int(input("Enter the ID value to select the row: "))
selected_row = df11[df11['ID'] == num]

# Print the selected row
print("Row with ID value of num:")
print(selected_row)