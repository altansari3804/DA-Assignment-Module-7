#80) Write a Python program to count the frequency of words in a file.

# Function to count the frequency of words in a file
def count_word_frequency(filename):
    word_frequency = {}
    with open(filename, "r") as file:
        # Read the file line by line
        for line in file:
            words = line.split()  # Split the line into words
            for word in words:
                word = word.lower()  # Convert to lowercase to count case-insensitively
                word_frequency[word] = word_frequency.get(word, 0) + 1  # Update the word count

    return word_frequency

# Example usage
word_count = count_word_frequency("example.txt")
for word, frequency in word_count.items():
    print(f"{word}: {frequency}")
