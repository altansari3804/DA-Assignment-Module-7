#73) Write a Python program to append text to a file and display the text.


# Append text to the file
with open("example.txt", "a") as file:
    file.write("This is the appended text.\n")

# Read and display the updated content of the file
with open("example.txt", "r") as file:
    content = file.read()

print(content)

