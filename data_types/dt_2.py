# Write a Python program to get a string made of the first 2 and the last 2 charsfrom a given a string. If the string length is less than 2, return instead of the empty string.

def str_both_end(string):
    if len(string)<2:
        return ''
    else:
        return string[0:2]+string[-2:]
print(str_both_end("Python"))
print(str_both_end("Py"))
print(str_both_end("P"))