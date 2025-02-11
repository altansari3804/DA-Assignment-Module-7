#9) Write python program that swap two number with temp variable and without temp variable. 

#Using temp variable.

n=int(input("enter a number N:"))
n1=int(input("enter a number N1:"))
temp=n
n=n1
n1=temp
print("After swaping N:",n)
print("After swaping N1:",n1)


#without Using temp variable.
n=int(input("enter a number N:"))
n1=int(input("enter a number N1:"))
n,n1=n1,n
print("After swaping N:",n)
print("After swaping N1:",n1)



