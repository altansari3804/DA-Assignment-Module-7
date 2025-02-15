#72) Write a Python program to read an entire text file. 


# Open the file in read mode
with open("example.txt", "r") as file:
    # Read the entire content of the file
    content = file.read()

# Print the content of the file
print(content)
