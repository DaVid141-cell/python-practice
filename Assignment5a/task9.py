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
