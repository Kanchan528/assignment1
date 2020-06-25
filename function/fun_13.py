#Write a Python program to sort a list of tuples using Lambda.

def main():
    tuple_list=[("Kanchan",22),("Samundra",19),("Usha",23)]
    tuple_list.sort(key= lambda x: x[1])
    print(tuple_list)

if __name__=='__main__':
    main()