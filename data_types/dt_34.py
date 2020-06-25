# Write a Python script to merge two Python dictionaries.

dic1={"name":"Kanchan", "address":"Baneshowr"}
dic2={"name":"Muskan", "address":"Sukedhara"}
dic3={}
for d in [dic1,dic2]:
    dic3.update(d)
print(dic3)