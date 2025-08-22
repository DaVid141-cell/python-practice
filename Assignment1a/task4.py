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
