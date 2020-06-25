# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

def match_char(words):
    result=0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            result = result+1
    return result
print(match_char(["aba","abc","hgh","123"]))


