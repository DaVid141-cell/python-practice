## Task 1: Opening and Reading a File
# Write a program that opens a file named sample.txt in read mode and prints its content.

read_file = open('sample.txt', 'r')

content_file = read_file.read()

print(read_file)
# This prints the actual content of the file
print(content_file)