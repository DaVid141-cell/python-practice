## Task 1: Opening and Reading a File
# Write a program that opens a file named sample.txt in read mode and prints its content.

read_file = open('sample.txt', 'r')

content_file = read_file.read()

print(read_file)
# This prints the actual content of the file
print(content_file)

## Task 2: Reading a Specific Number of Characters
# Modify the previous task to read only the first 10 characters of the file.

read_file = open('sample.txt', 'r')

# Read the first 10 characters
content_file = read_file.read(10)

print(content_file)

## Task 3: Using .readlines() Method
# Write a program that reads all lines of a file into a list and prints them one by one.

read_file = open('sample.txt', 'r')

file_lines = read_file.readlines()

# Loop through the list and print each line
for line in file_lines:
    print(line)

## Task 4: Using .readline() Method
# Modify the program to read only the first line of the file.

read_file = open('sample.txt', 'r')

# Read the first line only
line1 = read_file.readline()
print(line1)

## Task 5: Using .strip() Method with Arguments
# Given a file with extra spaces or newlines, read its content and remove unwanted spaces.

read_file = open('sample.txt', 'r')

# First: Open and read the file, but print each line as it is (with spaces/newlines)
with open('sample.txt', 'r') as read_file:
    file_line = read_file.readline()
    while file_line:
        print(file_line)  # prints with spaces/newlines
        file_line = read_file.readline()

# Second: Open and read the file, but clean each line using .strip()
with open('sample.txt', 'r') as read_file:
    for line in read_file:
        print(line.strip())