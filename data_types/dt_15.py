# Write a Python function to insert a string in the middle of a string.

def insert_string(string, word):
    return string[0:2] + word + string[2:]
print(insert_string("[[]]", "Python"))
print(insert_string("{{}}", "PHP"))
