#36) Write a Python function that takes a list and returns a new list with unique elements of the first list.

def get_unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

input_list = [1, 2, 3, 2, 4, 1, 5]
unique_list = get_unique_elements(input_list)
print("List with unique elements:", unique_list)




 