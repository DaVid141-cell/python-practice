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