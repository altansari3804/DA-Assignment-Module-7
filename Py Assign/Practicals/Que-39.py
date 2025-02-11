#39) Write a Python program to find the second smallest number in a list.

def second_smallest(input_list):
    unique_list = sorted(set(input_list))
    
    if len(unique_list) >= 2:
        return unique_list[1]
    else:
        return None
        
my_list = [5, 2, 8, 7, 1, 2, 3]
result = second_smallest(my_list)
print("The second smallest number is:", result)


