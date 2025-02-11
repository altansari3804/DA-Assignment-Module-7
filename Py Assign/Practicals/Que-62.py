#62) Write a Python function to check whether a number is in a given range 

def in_range(num, start, end):
    return start <= num <= end

number=int(input("Enter a Number:"))
start=1
end=10
if in_range(number,start,end):
        print(f"{number} is in the range!!!")
else:
        print(f"{number} is not in the range!!!")
