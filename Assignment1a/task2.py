# Task 2: If Comparison and String Comparison

# Get user input for favorite color and number
favorite_color = input("Input your Favorite Color: ")
number = input("Input your Favorite Number: ")

# Convert number to integer
number = int(number)

# Check conditions
if favorite_color.lower() == "blue" and number > 10:
    print("Great choice!")
else:
    print("Nice selection!")
