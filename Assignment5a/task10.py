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