#77) Write a Python program to read a file line by line store it into a variable.

# Function to read a file line by line and store it into a variable
def read_file_to_variable(filename):
    content = ""
    with open(filename, "r") as file:
        for line in file:
            content += line  # Append each line to the variable
    return content

# Example usage
file_content = read_file_to_variable("example.txt")
print(file_content)

