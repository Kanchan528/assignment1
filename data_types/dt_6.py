# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

def string_operate(string):
    if 'not' in string and 'poor' in string:
        s_not=string.find('not')
        s_poor=string.find('poor')
        if s_not < s_poor:
            return string.replace(string[s_not:],'good')
    return string

def main():
    string = input("Input String: ")
    print(string_operate(string))

if __name__ == "__main__":
    main()