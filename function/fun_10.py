#Write a Python program to print the even numbers from a given list.

def even_num(n):
    enum = []
    for i in n:
        if i % 2 == 0:
            enum.append(i)
    return enum
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))