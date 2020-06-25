#Write a Python program to check whether a given string is number or not using Lambda.

def main():
    string= input('Enter input: ')
    result=string.replace('.','')
    print("is number= ",result.isdigit())

if __name__ == '__main__':
    main()
