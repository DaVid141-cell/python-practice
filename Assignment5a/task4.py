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