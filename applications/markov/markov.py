import random

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()
    # split it into words.
    words = words.split()

# put every words to key
# test = ["Cats", "and", "dogs", "and", "birds"]
myDict = {}
length = len(words)
for i in range(length-1):
    w = words[i]
    if w not in myDict:
        myDict[w] = []
    # if exists in myDict, add it to the value(array type):
    myDict[w].append(words[i+1])

# Your code here

# get start words
start_words = []
for k in myDict:
    condition = k[0] == '"' and k[1].isupper()
    if k[0].isupper() or condition:
        start_words.append(k)

# get stop words
stop_words = []
for k in myDict:
    conditionA = k[len(k)-2] == "." and k[len(k)-1] == '"'
    conditionB = k[len(k)-2] == "?" and k[len(k)-1] == '"'
    conditionC = k[len(k)-2] == "!" and k[len(k)-1] == '"'
    if conditionA or conditionB or conditionC or k[len(k)-1] == "!" or k[len(k)-1] == "?" or k[len(k)-1] == ".":
        stop_words.append(k)

start = random.choice(start_words)
stop = random.choice(stop_words)
print("start:", start)
print("end:", stop)


cur = start
while cur is not stop:
    print(cur, end=" ")
    print(random.choice(myDict[cur]), end=" ")
    cur = random.choice([*myDict])
print(stop)
