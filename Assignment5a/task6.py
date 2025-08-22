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