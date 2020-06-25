# Write a Python script to check whether a given key already exists in a
# dictionary.

dic={"a":20,"b":30,"c":40}
def check_key(a):
    if a in dic.keys():
        print("This key is present in dictionary.")
    else:
        print("Sorry!!")
check_key("a")
check_key(3)