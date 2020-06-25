# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
    x=[]
    for a in l:
        if a not in x:
            x.append(a)
    return x

def main():
    list1=list(map(int,input().split(' ')))
    result=unique_list(list1)
    print("Unique list is: ",result)

if __name__=='__main__':
    main()