#81) Write a Python program to write a list to a file.

# Function to write a list to a file
def write_list_to_file(filename, data_list):
    with open(filename, "w") as file:
        for item in data_list:
            file.write(str(item) + "\n")  # Write each item to the file, each on a new line

# Example usage
data = ["apple", "banana", "cherry", "date"]
write_list_to_file("example.txt", data)
