def hash(word, size):
    total = 0
    for x in range(len(word)):
        c = word[x]
        total = total + ord(c)
        total = total * 101

    return total % size

