# Write a Python program to remove an item from a tuple.

tuple1=(1,2,3,4,5)
print(tuple1)
list1=list(tuple1)
list1.remove(3)
tuple1=tuple(list1)
print(tuple1)