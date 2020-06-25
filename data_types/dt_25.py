# Write a Python program to check whether all dictionaries in a list are empty or
# not.

list1=[{},{},{}]
list2=[{1,2},{2},{4}]
print(all(not a for a in list1))
print(all(not a for a in list2))
