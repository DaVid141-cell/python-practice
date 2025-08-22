## Task 4: Using Methods on Lists
# Create a list of numbers and demonstrate append(), remove(), and sort() methods.

def method_list(input_add, input_remove):
    my_list = ["java", "php", "python", "c++", "ruby"]

    my_list.append(input_add)
    after_append = my_list.copy()

    for item in my_list:
        if item.lower() == input_remove.lower():
            my_list.remove(item)
            break
    after_remove = my_list.copy()

    my_list.sort()
    after_sort = my_list.copy()
    
    return after_append, after_remove, after_sort

# Get user input for append and remove
input_add = input("Add Data: ")
input_remove = input("Remove Data: ")

after_append, after_remove, after_sort = method_list(input_add, input_remove)


print("List after append: ", after_append)
print("\nList after remove: ", after_remove)
print("\nList after sorting: ", after_sort)