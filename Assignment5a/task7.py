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
