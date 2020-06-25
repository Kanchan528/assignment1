#Write a Python program to create Fibonacci series upto n using Lambda.
from functools import reduce

def main():
    num=int(input('Length of Fibonacci series: '))
    fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]], range(n-2), [0, 1]) 
    print(fib(num))


if __name__ == '__main__':
    main()
