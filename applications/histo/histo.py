# Your code here
import string

with open("robin.txt") as f:
    words = f.read()

# words = "dog, dog, dog, hot, hot, cat, car"

# # remove punctuation
for c in string.punctuation:
    # except '
    if c != "'":
        words = words.replace(c, "")

# split it into words.
words = words.split()
counts = {}

for w in words:
    if w not in counts:
        counts[w] = []
    counts[w].append("#")

# find longest word:
logest_str = max(words, key=len)
longest_len = len(logest_str)

myDict = sorted(counts.items(), key=lambda item: item[1], reverse=True)
# print(type(myDict))
for k, v in myDict:
    if len(k) < longest_len:
        k = k+" "*(longest_len-len(k))
    print(k, end=" ")
    print("".join(v))
