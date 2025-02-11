#48) Write a Python script to sort (ascending and descending) a dictionary by value. 

d= {'a': 10, 'b': 20, 'c': 5, 'd': 15}

asc = dict(sorted(d.items(), key=lambda item: item[1]))

desc = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Ascending order:", asc)
print("Descending order:",desc)

