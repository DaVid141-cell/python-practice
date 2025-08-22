## Task 1: Creating and Calling Functions
# Write a function greet_user that takes a name as input and prints a greeting message.

# Function to greet the user
def greet(user):
    print(f"Hello {user}, nice to meet you!")
   
# Get user input
user = input("Enter your username: ")

# Call the function with the user input
greet(user)