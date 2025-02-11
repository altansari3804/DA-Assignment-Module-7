#5) Write a Python program to get the Factorial number of given numbers.


n=int(input("Enter a Number:"))
i=1
fac=1

while(i<=n):
    fac*=i
    i+=1
    print(fac)
