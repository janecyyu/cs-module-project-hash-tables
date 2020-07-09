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

for k, v in counts.items():
    print(k, end=" ")
    print("".join(v))
