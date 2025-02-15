#74) Write a Python program to read first n lines of a file.

# Function to read first n lines of a file
def read_first_n_lines(filename, n):
    with open(filename, "r") as file:
        for i in range(n):
            line = file.readline()
            if not line:  # End of file reached
                break
            print(line, end='')

# Example usage
n = 5  # Number of lines to read
read_first_n_lines("example.txt", n)

