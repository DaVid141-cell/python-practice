## Task 2: Reading a Specific Number of Characters
# Modify the previous task to read only the first 10 characters of the file.

read_file = open('sample.txt', 'r')

# Read the first 10 characters
content_file = read_file.read(10)

print(content_file)