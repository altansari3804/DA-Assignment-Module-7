#50) Write a Python script to check if a given key already exists in a dictionary.

d={'a':1,'b':2,'c':3}
print(d)
key=input("enter a key :")

if key in d:
    print("The key is exists in a dictionary!!!")
else:
    print("The key is not exists in a dictionary!!!")
