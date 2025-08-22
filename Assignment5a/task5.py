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
