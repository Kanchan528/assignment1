# Write a Python program to square and cube every number in a given list of integers using Lambda.

def main():
    list1=[1,2,3,4,5]
    square_list1=map(lambda x: x**2,list1)
    print("square of list is: ",list(square_list1))
    cube_list1= map(lambda x: x**3,list1)
    print("cube of list is ",list(cube_list1))

if __name__ == "__main__":
    main()