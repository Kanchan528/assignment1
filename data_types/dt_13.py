# Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

item=input('Enter comma seperated words')
words = item.split(' ')
words.sort()
print("The sorted words are: ")
for word in words:
    print(word)