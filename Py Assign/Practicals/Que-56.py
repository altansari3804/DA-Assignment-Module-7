#56) Write a Python program to map two lists into a dictionary 
#Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300}).


keys = ['a', 'b', 'c', 'd']
values = [400, 400, 300, 400]

d= dict(zip(keys, values))

d1= dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

print("Counter", d1)
