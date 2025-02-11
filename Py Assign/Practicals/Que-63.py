#63) Write a Python function to check whether a number is perfect or not.

def perfect(number):
    divisors_sum = sum(i for i in range(1, number) if number % i == 0)
    
    return divisors_sum == number

number = 6
if perfect(number):
    print(f"{number} is a perfect number")
else:
    print(f"{number} is not a perfect number")
