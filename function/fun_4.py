# Write a Python program to reverse a string.

def reverse_string(string):
    return string[-1::-1]

def main():
    string=input('Enter any word: ')
    print("The reverse is: ",reverse_string(string))

if __name__=='__main__':
    main()
