import string


def word_count(s):
    # remove punctuation
    for c in string.punctuation:
        # except '
        if c is not "'":
            s = s.replace(c, "")
    counts = {}
    s = s.lower()
    s = s.split()
    for word in s:
        if word not in counts:
            counts[word] = 0
        counts[word] += 1
    # print("counts", counts)
    return counts


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
