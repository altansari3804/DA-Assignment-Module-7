#79) Write a Python program to count the number of lines in a text file.

# Function to count the number of lines in a file
def count_lines_in_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()  # Read all lines from the file
        return len(lines)  # Return the number of lines

# Example usage
line_count = count_lines_in_file("example.txt")
print("Number of lines in the file:", line_count)


