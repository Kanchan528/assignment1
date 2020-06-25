# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def check_upper_lower(word):
    upperCase=0
    lowerCase=0
    for i in word:
        if i.isupper():
            upperCase+=1
        elif i.islower():
            lowerCase+=1
        else:
            pass
    return upperCase, lowerCase

def main():
    word=input("Enter anything: ")
    result=check_upper_lower(word)
    print("the number of upper case and number of lowercase is: ",result)

if __name__=='__main__':
    main()