#49) Write a Python script to concatenate following dictionaries to create a new one.

d1= {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

d= {**d1, **d2, **d3}

print("New concatenated dictionary:", d)

