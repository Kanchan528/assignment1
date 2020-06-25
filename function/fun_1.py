# Write a Python function to find the Max of three numbers

def find_max(a,b,c):
    if a>b:
        if a>c:
            maxNumber = a
        else:
            maxNumber = c
    elif b>c:
        maxNumber = b
    else:
        maxNumber = c
    return maxNumber
def main():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=int(input("Enter third number: "))
    maximum=find_max(a,b,c)
    print("Maximum number is: ",maximum)

if __name__=='__main__':
    main()