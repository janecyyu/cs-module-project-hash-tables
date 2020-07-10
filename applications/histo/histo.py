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
words = words.lower()
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

# make dict to list
dictlist = []
temp = []

for key, value in counts.items():
    temp = [key, value]
    dictlist.append(temp)

dictlist = sorted(dictlist, key=lambda item: (-len(item[1]), item[0]))

for k, v in dictlist:
    if len(k) < longest_len:
        k = k+" "*(longest_len-len(k))
    print(k, end=" ")
    print("".join(v))
