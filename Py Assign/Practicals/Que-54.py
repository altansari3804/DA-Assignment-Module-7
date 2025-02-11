#54) Write a Python program to check multiple keys exists in a dictionary

d={'a': 1, 'b': 2, 'c': 3}
n= ['a','b','c']

if all(key in d for key in n):
    print("All keys are exist")
else:
    print("Some keys are missing")
