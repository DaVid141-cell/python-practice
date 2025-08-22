## Task 5: For Loop and Ternary Operator
# Write a program that prints whether each number in a range from 1 to 20 is even or odd.

#start_number = int(input("Enter the start number: "))
#end_number = int(input("Enter the end number: "))

for number in range(1, 21):
   
    # Use a ternary operator to determine if the number is even or odd
    result = "even" if number % 2 == 0 else "odd"
    print(f"The number {number} is {result}.")




