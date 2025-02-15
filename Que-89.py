#89) How Do You Handle Exceptions with Try/Except/Finally in Python?
#Explain with coding snippets. 

try:
    # Code that might raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2  # Division operation may raise ZeroDivisionError
except ZeroDivisionError:
    # Code to handle division by zero error
    print("Error: Cannot divide by zero!")
except ValueError:
    # Code to handle invalid input (non-numeric values)
    print("Error: Please enter valid integers!")
else:
    # Code that runs if no exceptions occurred
    print(f"The result of the division is: {result}")
finally:
    # Code that will always run (cleanup code)
    print("Execution completed.")
