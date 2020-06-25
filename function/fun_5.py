# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

def find_factorial(num):
    factorial=1
    if num<0:
        print("The factorial of this number does not exist")
    else:
        for i in range(1,num+1):
            factorial=factorial*i
    return factorial

def main():
    number=int(input("Enter the number: "))
    result=find_factorial(number)
    print('The factorial of number is: ',result)

if __name__=='__main__':
    main()        