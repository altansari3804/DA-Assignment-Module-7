#64) Write a Python function that checks whether a passed string is palindrome or not

def palindrome(s):
    s = s.replace(" ", "").lower()
    
    return s == s[::-1]

str=input("Enter a string: ")

if palindrome(str):
    print(f"'{str}' is a palindrome!!")
else:
    print(f"'{str}' is not a palindrome!!")

