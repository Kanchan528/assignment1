# Write a Python program to sort a list of dictionaries using Lambda.

def main():
    dic=[{'name':'Kripa', 'age':23, 'address':'Bhaktapur'},{'name':'Supraja', 'age':15, 'address':'Sukedhara'}]
    dic.sort(key=lambda x: x['age'])
    print(dic)

if __name__ == "__main__":
    main()