#61) Write a Python function to calculate the factorial of a number (a  nonnegative integer) 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number:"))
print(f"Factorial of {number} is {factorial(number)}")


