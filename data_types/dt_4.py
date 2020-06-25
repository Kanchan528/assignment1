# Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.

def swap_char(a,b):
    a_new = b[:2]+a[2:]
    b_new = a[:2]+b[2:]
    return (a_new + ' ' + b_new)
print(swap_char("abcd", "wxyz"))