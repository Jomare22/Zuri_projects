# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    sentences = open(filename)
    return sentences

def count_words():
    text = read_file_content('story.txt')
    # [assignment] Add your code here
    dictionary = dict()
    for line in text:
        line = line.rstrip()
        words = line.split()
        for i in words:
            if i in dictionary: #counting existing words
                dictionary[i] = dictionary[i] + 1
            else: #counting new words
                dictionary[i] = 1

    return dictionary

print(count_words())
