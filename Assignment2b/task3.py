#Task 3: Looping Through a List
# Write a program that prints each element in the list with its index and length of the name.

array = ["java", "php", "python", "c++", "ruby"]

for index, lang in enumerate(array):
    print(f"index:{index}, array: {lang}, length:{len(lang)} ")

#enumerate(array) to index and lang gives the value of each item in the list
#len(lang) will identify the length of each word in the list

