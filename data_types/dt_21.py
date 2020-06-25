# Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.

def find_last(num):
    return num[-1]  
  
def sort_list_last(tuples):
    return sorted(tuples, key=find_last)  
  
print(sort_list_last([(1,2),(5,6),(3,4),(8,9),(3,8)]))  


