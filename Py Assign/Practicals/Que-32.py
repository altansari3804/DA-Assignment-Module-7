#32) Write a Python program to remove duplicates from a list. 

def remove_duplicates(n):
    return list(set(n))

n=input("Enter a List:")
result = remove_duplicates(n)
print("List after removing duplicates:", result)
 