#59) Write a Python program to create a dictionary from a string.
#Note: Track the count of the letters from the string.


n= input("Enter a string:")

count = {}

for char in n:
    if char != ' ':
        count[char] = count.get(char, 0) + 1

print("Letter count:", count)
