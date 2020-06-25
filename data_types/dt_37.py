# Write a Python program to multiply all the items in a dictionary.

dic={1:3,2:4}
mul=1
for key in dic:
    mul*=dic[key]
print(mul)