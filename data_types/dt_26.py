# Write a Python program to insert a given string at the beginning of all items in
# a list

stri="Apple"
list1=[1,2,3]
stri += '% s'
list1 =  [stri % i for i in list1] 
print(list1)
