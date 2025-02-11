#38) Write a Python program to select an item randomly from a list.

import random

def select_random_item(n):
    return random.choice(n)

list = [10, 20, 30, 40, 50]
random_item = select_random_item(list)
print("Randomly selected item:", random_item)


