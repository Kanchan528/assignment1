# Write a Python program to sum all the items in a list.

def sum_of_number(num):
    result = 0
    for n in num:
        result = result+n
    return result
print(sum_of_number([-2,4,5,-6,7]))