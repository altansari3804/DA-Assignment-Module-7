#75) Write a Python program to read last n lines of a file.

# Function to read last n lines of a file
def read_last_n_lines(filename, n):
    with open(filename, "r") as file:
        # Read all lines and get the last n lines
        lines = file.readlines()
        last_n_lines = lines[-n:]

    # Print the last n lines
    for line in last_n_lines:
        print(line, end='')

# Example usage
n = 5  # Number of lines to read from the end
read_last_n_lines("example.txt", n)
