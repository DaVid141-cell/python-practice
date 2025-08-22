# Task 1: Creating and Subsetting Lists
# Create a list of five programming languages.
# Print the first, third, and last elements of the list.

import numpy as np

array = np.array(["java", "php", "python", "c++", "ruby"])

elements = array[[0, 2, 4]]

print(elements)

# Task 2: Manipulating Lists
# Add "Swift" and "Go" to the list and remove "Ruby".

array = ["java", "php", "python", "c++", "ruby"]

array.append("swift")
array.append("go")

array.remove("ruby")

print(array)

#Task 3: Looping Through a List
# Write a program that prints each element in the list with its index and length of the name.

#enumerate(array) to index and lang gives the value of each item in the list
#len(lang) will identify the length of each word in the list

array = ["java", "php", "python", "c++", "ruby"]

for index, lang in enumerate(array):
    print(f"index:{index}, array: {lang}, length:{len(lang)} ")


#Task 4: Checking Membership
# Ask the user to enter a language name and check if it exists in the list.
# If found, display its index, else print a message that it is not found.

array = ["java", "php", "python", "c++", "ruby"]

language = input("Enter a Programing language: ")

if language.lower() in array:
    print(array.index(language.lower()))
else:
    print("Language not found!")
    

#Task 5: Sorting and Reversing a List
# Sort the list in alphabetical order and then reverse it.

array = ["java", "php", "python", "c++", "ruby"]

array.sort()
#['c++', 'java', 'php', 'python', 'ruby']
array.reverse()
#['ruby', 'python', 'php', 'java', 'c++']

print(array)

#Task 6: List Comprehension
# Create a list of square numbers for values from 1 to 10 using list comprehension.

square = [number ** 2 for number in range(1,11)]
print(square)


#Task 7: Removing Duplicates from a List
# Given a list of numbers with duplicates, remove duplicates and print the unique values.

numbers = [1, 1, 2, 2, 2, 3, 3, 4, 5, 5,]

unique_numbers = list(set(numbers))

print(unique_numbers)