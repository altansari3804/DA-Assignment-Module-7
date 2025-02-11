#42) Write a Python program to split a list into different variables.


def split_list(input_list):
    a,b,c= input_list
    return a,b,c

input_list = [10, 20, 30,]
a,b,c= split_list(input_list)

print("A:", a)
print("B:", b)
print("C:", c)
