#12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 


a=int(input("enter a number:"))
b=int(input("enter a number:"))
c=int(input("enter a number:"))

if a==b or b==c or a==c:
    print("the sum is 0 because two values are same")

else:
    total=a+b+c
    print("sum of three numbers is:",total)