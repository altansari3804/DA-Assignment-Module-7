#10) Write a Python program to find whether a given number is even 
# or odd, print out an appropriate message to the user. 

n=int(input("Enter a Number:"))

if n==0:
    print("Number is neither even or odd!!!")

elif n%2==0:
    print("Number is Even!!!")

else:
    print("Number is Odd!!!")