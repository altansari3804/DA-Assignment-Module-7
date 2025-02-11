#6) Write a Python program to get the Fibonacci series of given range.


n=int(input("Enter a Number:"))
a=0
b=1
print("Fibonacci Series:")
for i in range(n):
    print(a,end="")
    a=b
    b=a+b
