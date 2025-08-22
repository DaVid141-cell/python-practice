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