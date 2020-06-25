#Write a Python program to filter a list of integers using Lambda.

def main():
    list1=[2,4,5,6,6.6,8.8,-3,7,-2]
    filter_list=filter(lambda x: isinstance(x,int), list1)
    print(list(filter_list))

if __name__ == "__main__":
    main()