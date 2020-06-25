# Write a Python function to create the HTML string with tags around the word(s).

def add_tag(tag, word):
    return "<%s> %s </%s>" %(tag,word, tag)

print(add_tag("i","Python"))
print(add_tag("b","Python"))