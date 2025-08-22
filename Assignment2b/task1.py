import numpy as np

# Task 1: Creating and Subsetting Lists
# Create a list of five programming languages.
# Print the first, third, and last elements of the list.

array = np.array(["java", "php", "python", "c++", "ruby"])

elements = array[[0, 2, 4]]

print(elements)
