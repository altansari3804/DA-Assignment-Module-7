#35) Write a Python program to generate and print a list of first and last 5
#elements where the values are square of numbers between 1 and 30.


def square_list():
    square_list = []
    
    for x in range(1, 31):
        square_list.append(x**2)
    
    print("First 5 elements:", square_list[:5])
    print("Last 5 elements:", square_list[-5:])

square_list()
