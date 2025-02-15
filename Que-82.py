#82) Write a Python program to copy the contents of a file to another file.


# Function to copy contents from one file to another
def copy_file_contents(source_file, destination_file):
    with open(source_file, "r") as src:
        content = src.read()  # Read the entire content of the source file

    with open(destination_file, "w") as dest:
        dest.write(content)  # Write the content to the destination file

# Example usage
copy_file_contents("source.txt", "destination.txt")
