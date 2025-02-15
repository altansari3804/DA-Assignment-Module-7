#78) Write a python program to find the longest words.

# Function to find the longest word(s)
def find_longest_words(text):
    words = text.split()  # Split the text into a list of words
    longest_length = max(len(word) for word in words)  # Find the length of the longest word
    longest_words = [word for word in words if len(word) == longest_length]  # Get all longest words
    return longest_words

# Example usage
text = "This is a sample text with several long words"
longest_words = find_longest_words(text)
print("Longest word(s):", longest_words)

