# Write a Python function that takes a list of words and returns the length of the longest one.

def find_longest_word(text):
    longest_word = max(text.split())
    return longest_word, len(longest_word)

def main():
    text=input("Enter text: ")
    result=find_longest_word(text)
    print(result)

if __name__ == "__main__":
    main()
