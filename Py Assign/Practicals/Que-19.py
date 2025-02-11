#19) Write a Python program to count the occurrences of each word in a given sentence.

str=input("Enetr a String:")
chr=input("Enter a Character:")
count=0

for i in str:
    if chr==i:
        count=count+1

print("The Occurrences of word is:",count)