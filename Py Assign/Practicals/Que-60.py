#60) Sample string:  
#'w3resource' Expected output: {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1} 

n= 'w3resource'
count = {}

for char in n:
    count[char] = count.get(char, 0) + 1

print(count)
