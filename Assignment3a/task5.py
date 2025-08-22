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




