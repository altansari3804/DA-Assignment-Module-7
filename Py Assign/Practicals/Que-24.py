#24) Write a Python function to insert a string in the middle of a string. 

str=input("Enter a String: ")
substr=input("Enter a Substring:")

n=len(str)//2
n1=str[:n]+substr+str[n:]

print(n1)