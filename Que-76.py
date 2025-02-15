#76) Write a Python program to read a file line by line and store it into a list

# Function to read a file line by line and store it into a list
def read_file_to_list(filename):
    with open(filename, "r") as file:
        lines = file.readlines()  # Reads all lines and stores them in a list
    return [line.strip() for line in lines]  # Remove any extra newline characters

# Example usage
file_lines = read_file_to_list("example.txt")
print(file_lines)

