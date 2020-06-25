# Write a Python function that takes a number as a parameter and check the number is prime or not.

def prime(n):
    if n==1:
        return False
    for i in range(2,n):
        if n % i == 0:
            flag = False
            break
    else:
        flag = True
    return flag

def main():
    n=int(input("Enter number: "))
    result = prime(n)
    if result==True:
        print(n, "is prime number")
    else:
        print(n, "is not prime number")

if __name__=='__main__':
    main()