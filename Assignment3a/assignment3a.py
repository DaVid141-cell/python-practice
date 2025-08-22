## Task 1: Creating and Calling Functions
# Write a function greet_user that takes a name as input and prints a greeting message.

# Function to greet the user
def greet(user):
    print(f"Hello {user}, nice to meet you!")
   
# Get user input
user = input("Enter your username: ")

# Call the function with the user input
greet(user)

## Task 2: Function with Return Value
# Write a function square_number that takes a number as input and returns its square(s).

def square_number(num):
    # generate list of squares from 1 to n
    return num ** 2 

# Get user input
num = int(input("Enter a number: "))
result = square_number(num)

print(result)

## Task 3: Using Methods on Strings
# Given a string, use string methods to convert it to uppercase, lowercase, and check if it starts with a specific word

def string_methods(input_string):
    # Convert to uppercase
    upper_string = input_string.upper()
    # Convert to lowercase
    lower_string = input_string.lower()
    # Check if it starts with a specific word
    starts_with = input_string.startswith("hello")
    
    return upper_string, lower_string, starts_with

# Get user input
input_string = input("Enter a string: ")
result_upper, result_lower, starts_with_hello = string_methods(input_string)

print("Uppercase:", result_upper)
print("Lowercase:", result_lower)
print("Starts with 'Hello':", starts_with_hello)

## Task 4: Using Methods on Lists
# Create a list of numbers and demonstrate append(), remove(), and sort() methods.

def method_list(input_add, input_remove):
    my_list = ["java", "php", "python", "c++", "ruby"]

    my_list.append(input_add)
    after_append = my_list.copy()

    for item in my_list:
        if item.lower() == input_remove.lower():
            my_list.remove(item)
            break
    after_remove = my_list.copy()

    my_list.sort()
    after_sort = my_list.copy()
    
    return after_append, after_remove, after_sort

# Get user input for append and remove
input_add = input("Add Data: ")
input_remove = input("Remove Data: ")

after_append, after_remove, after_sort = method_list(input_add, input_remove)


print("List after append: ", after_append)
print("\nList after remove: ", after_remove)
print("\nList after sorting: ", after_sort)

## Task 5: Working with Packages
# Import the math package and use its methods to find the square root and factorial of a given number.

import math

def math_methods(number):
    # Calculate square root
    square_root = math.sqrt(number)
    # Calculate factorial
    factorial = math.factorial(number)
    
    return square_root, factorial

# Get user input
input_number = int(input("Enter a number: "))
square_root_result, factorial_result = math_methods(input_number)

print("Square root:", square_root_result)
print("Factorial:", factorial_result)