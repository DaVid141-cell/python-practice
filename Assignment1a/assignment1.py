## Task 1: Understanding Data Types and Variables
# Write a Python program that takes user input for their name, age, and height.
# Display the type of each input variable and convert age and height to appropriate types.

# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height in meters: ")

# Display the type of each input variable
print(f"Name: {name}, Type: {type(name)}")
print(f"Age: {age}, Type: {type(age)}")
print(f"Height: {height}, Type: {type(height)}")

#Convert age and height to appropriate types
age = int(age)  
height = float(height)

# Display the converted types
print(f"\nConverted Age: {age}, Type: {type(age)}")
print(f"Converted Height: {height}, Type: {type(height)}")

print("\nHello", name, "! You are", age, "years old and", height, "meters tall.")

## Task 2: If Comparison and String Comparison
# Write a program that asks for a user's favorite color and a number.
# If the color is "Blue" and the number is greater than 10, print "Great choice!" otherwise, print "Nice selection!"

# Get user input for favorite color and number
favorite_color = input("Input your Favorite Color:")
number = input("Input your Favorite Number:")

# Convert number to integer
number = int(number)

# Check conditions and print appropriate messages
if favorite_color.lower() == "Blue" and number > 10:
    print("Great choice!")
else:
    print("Nice selection!")



## Task 3: Nested Conditionals
# Create a program that takes a number as input and categorizes it as positive, negative, or zero.
# If the number is positive, further check if it is even or odd.

number = int(input("Enter a Number:"))
# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
    # Check if the positive number is even or odd
    if number % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
elif number < 0:
    print("The number is negative.")
elif number == 0:
    print("The number is zero.")
# Display the type of the input number
print(f"\nThe type of the input number is: {number} {type(number)}")


## Task 4: While True Loop with Boolean Comparisons
# Write a program that asks for a password and keeps asking until the correct password is entered.
# Also, limit the number of attempts to 3.

create_password = input("Create your own password:")
attempts = 3

print("Password is been saved!")

while attempts > 0:
    password = input("\nEnter the password: ")
    if password == create_password:
        print("\nAccess granted!")
        break
    else:
        attempts -= 1
        print(f"Incorrect password. You have {attempts} attempts left.")
        if attempts == 0:
            print("Access denied. No attempts left.")


## Task 5: For Loop and Ternary Operator
# Write a program that prints whether each number in a range from 1 to 20 is even or odd.


for number in range(1, 21):
   
    # Use a ternary operator to determine if the number is even or odd
    result = "even" if number % 2 == 0 else "odd"
    print(f"The number {number} is {result}.")


## Task 6: Looping with a Condition
# Write a program that sums up numbers from 1 to a user-given number using a while loop.

# Get user input for the upper limit
upper_limit = int(input("Enter a number to sum up to: "))

current_number = 1
total_sum = 0

while current_number <= upper_limit:
    total_sum += current_number
    current_number += 1


print(f"The total sum of numbers from 1 to {upper_limit} is: {total_sum}")
