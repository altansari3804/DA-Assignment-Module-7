#57) Write a Python program to find the highest 3 values in a dictionary

d= {'a': 400, 'b': 100, 'c': 300, 'd': 500, 'e': 200}

top_3 = dict(sorted(d.items(), key=lambda item: item[1], reverse=True)[:3])

print("Top 3 values:", top_3)
