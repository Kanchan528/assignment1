# Write a Python function to sum all the numbers in a list.

def sum_of_list(num):
    total=0
    for x in num:
        total = total+x
    return total
def main():
    number=list(map(int,input().split(' ')))
    result=sum_of_list(number)
    print("The sum of list is: ",result)
if __name__=='__main__':
    main()