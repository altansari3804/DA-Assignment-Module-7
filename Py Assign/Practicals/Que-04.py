#4) Write a Python program to check if a number is positive, negative or Zero

n=int(input("Enter a Number:"))
if n==0:
    print('neither positive nor negative')

elif n<0:
    print('Negative number')

else:
    print('Positive Number')