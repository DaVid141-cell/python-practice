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


