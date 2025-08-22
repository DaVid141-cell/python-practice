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
