# Write a Python function to check whether a number is in a given range.

def find_number_range(num):
    if num in range(1, num+1):
        print("The number is in given range.")
    else:
        print("The number is not in given range.")

def main():
    num=int(input("Enter the number: "))
    find_number_range(num)

if __name__=='__main__':
    main()
