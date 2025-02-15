#90) Write python program that user to enter only odd numbers, else will raise an exception. 

# Function to check if the number is odd
def get_odd_number():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:  # Check if the number is even
            raise ValueError("You entered an even number! Please enter an odd number.")
        print(f"Great! You entered the odd number: {num}")
    except ValueError as e:
        print(f"Error: {e}")
        get_odd_number()  # Prompt the user again for input

# Call the function
get_odd_number()
