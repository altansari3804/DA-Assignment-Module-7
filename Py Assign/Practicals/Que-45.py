#45) Write a Python program to unzip a list of tuples into individual lists.

tuple= [(1, 'a'), (2, 'b'), (3, 'c')]

a, b = zip(*tuple)

print("list1:", a)
print("list2:", b)




