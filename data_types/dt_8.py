# ​ Write a Python program to remove the n​ th​ index character from a nonempty string.

def remove_char(string,num):
    first=string[:num]
    last=string[num+1:]
    return first + last

print(remove_char('Apple',2))
print(remove_char('Banana',4))