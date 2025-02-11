#29) Write a Python function to get the largest number, smallest num and sum of all from a list.  

def get_largest_smallest_sum(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    total_sum = 0
    
    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
        total_sum += num

    return largest, smallest, total_sum

n= input("Enter a list: ")
n1= [int(x) for x in n.split()]

largest, smallest, total_sum = get_largest_smallest_sum(n1)

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print(f"Sum of all numbers: {total_sum}")
