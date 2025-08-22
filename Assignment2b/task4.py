#Task 4: Checking Membership
# Ask the user to enter a language name and check if it exists in the list.
# If found, display its index, else print a message that it is not found.

array = ["java", "php", "python", "c++", "ruby"]

language = input("Enter a Programing language: ")

if language.lower() in array:
    print(array.index(language.lower()))
else:
    print("Language not found!")
    