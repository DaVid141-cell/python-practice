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