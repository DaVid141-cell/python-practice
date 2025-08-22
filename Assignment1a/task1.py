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