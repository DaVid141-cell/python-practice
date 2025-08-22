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