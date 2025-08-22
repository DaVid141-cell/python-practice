## Task 4: Using .readline() Method
# Modify the program to read only the first line of the file.

read_file = open('sample.txt', 'r')

# Read the first line only
line1 = read_file.readline()
print(line1)