# Task 2: Function with Return Value
# Write a function square_number that takes a number as input and returns its square(s).

def square_number(num):
    # generate list of squares from 1 to n
    return num ** 2 

# Get user input
num = int(input("Enter a number: "))
result = square_number(num)

print(result)
