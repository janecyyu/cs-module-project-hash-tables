import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # split it into words.
    words = words.split()
# TODO: analyze which words can follow other words
# Your code here
# put every words to key
myDict = {}
length = words.len()
for i in range(length-1):
    w = words[i]
    if w not in myDict:
        arr = []
        myDict[w] = arr.append(words[i+1])
    # if exists in myDict, add it to the value(array type):
    myDict[w].append(words[i+1])


# TODO: construct 5 random sentences
# Your code here
