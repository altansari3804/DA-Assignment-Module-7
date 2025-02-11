#40) Write a Python program to get unique values from a list

def unique_values(input_list):
    return list(set(input_list))

my_list = [1, 2, 3, 4, 4, 5, 1, 2, 6]
unique_values = unique_values(my_list)
print("Unique values:", unique_values)

