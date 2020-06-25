# ​ Write a Python program to count the occurrences of each word in a given sentence.

def count_each_word(string):
    count=dict()
    words=string.split(' ')

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

print(count_each_word("the quick brown fox jumps over the lazy dog."))