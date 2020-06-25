# Write a Python program to replace the last element in a list with another list.

list1=[1,3,5,7,9]
list2=[2,4,6,8]
list1 = list1[:-1]+list2
print(list1)