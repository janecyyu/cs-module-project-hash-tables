def no_dups(s):
    # Your code here
    if s is "":
        return s

    counts = {}
    # slipt each word
    s = s.split()
    # count the words
    for w in s:
        if w not in counts:
            counts[w] = 0
        counts[w] += 1

    result = []
    # put the keys to result
    for key in counts:
        result.append(key)

    # convert list to string
    result = ' '.join(map(str, result))
    return result


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
