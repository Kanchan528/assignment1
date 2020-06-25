# Write a Python program to count the number of characters (character frequency) in a string.

input_string="google.com"
dict={}
for x in input_string:
    if x in dict:
        dict[x]=dict[x]+1
    else:
        dict[x]=1
print(dict)