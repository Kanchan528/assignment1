# Write a Python program to multiplies all the items in a list.

def multiple_of_number(num):
    result = 1
    for n in num:
        result=result*n
    return result
print(multiple_of_number([2,4,2]))