## Task 3: Using .readlines() Method
# Write a program that reads all lines of a file into a list and prints them one by one.

read_file = open('sample.txt', 'r')

file_lines = read_file.readlines()

# Loop through the list and print each line
for line in file_lines:
    print(line)