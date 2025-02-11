#41) Write a Python program to check whether a list contains a sub list


def contains_sublist(main_list, sublist):
    for i in range(len(main_list) - len(sublist) + 1):
        if main_list[i:i + len(sublist)] == sublist:
            return True
    return False

main_list = [1, 2, 3, 4, 5, 6]
sublist = [3, 4]
result = contains_sublist(main_list, sublist)
print("The list contain the sublist", result)

sublist2 = [7, 8]
result2 = contains_sublist(main_list, sublist2)
print("The list contain the sublist", result2)
