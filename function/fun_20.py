# Write a Python program to find intersection of two given arrays using Lambda.

def main():
    array1=[2,3,4,5,6,7,8]
    array2=[4,5]
    intersection=list(filter(lambda a: a in array1,array2))
    print(intersection)

if __name__ == "__main__":
    main()