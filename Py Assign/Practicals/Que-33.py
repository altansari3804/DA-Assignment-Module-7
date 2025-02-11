#33) Write a Python program to check a list is empty or not.

def is_list_empty(n):
    if not n:
        return "The list is empty."
    else:
        return "The list is not empty."

n= []
result = is_list_empty(n)
print(result)

n= [1, 2, 3]
result = is_list_empty(n)
print(result)

