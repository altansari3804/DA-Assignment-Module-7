#18) Write a Python program to count occurrences of a substring in a string. 

def substroccur(substr):
    str="i am python developer, python is programing language, python is simple to learn."
    newstr=str.split()
    count=0
    for i in newstr:
        if substr==i:
            count+=1
    return count

inputstr="python"
print(f"the count of {inputstr} in str is {substroccur(inputstr)}")
