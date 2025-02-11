#20) Write a Python program to get a single string from two given strings,
#separated by a space and swap the first two characters of each string.


str1 = "hello"
str2 = "world"

if len(str1) >= 2 and len(str2) >= 2:
    str1_swapped = str2[:2] + str1[2:]
    str2_swapped = str1[:2] + str2[2:]
else:
    str1_swapped = str1
    str2_swapped = str2

result = str1_swapped + " " + str2_swapped

print(result)
