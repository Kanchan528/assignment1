# Write a Python function to multiply all the numbers in a list.

def multiple_of_list(num):
    product=1
    for i in num:
        product = product*i
    return product

def main():
    number=list(map(int,input().split(' ')))
    result=multiple_of_list(number)
    print("The multiple of list is: ",result)

if __name__=='__main__':
    main()