def hash(word, size):
    total = 0
    for x in range(len(word)):
        c = word[x]
        total = total + ord(c)
        total = total * 101

    return total % size


# Question 2
def h(n, S):
    return n % S


def Q2(insert_list, S=10):
    result = []
    for i in insert_list:
        result.append((i, h(i, S)))

    return result


# Question 3:

def rehash(k, n, S):
    return (h(n, S) + k) % S


def Q3(insert_list, S=10):
    result = {0: None,
              1: None,
              2: None,
              3: None,
              4: None,
              5: None,
              6: None,
              7: None,
              8: None,
              9: None, }
    for num in insert_list:
        for k in range(S):
            key = rehash(k, num, S)
            if result[key] == num:
                pass
            if result[key] == None:
                result[key] = num
                break
    return result



if __name__ == "__main__":
    # a = [45, 27, 100, 20, 9, 24, 2, 13, 50, 12]
    # print(Q3(a, 10))
    # b = [9, 13, 14, 3, 21]
    # print(Q3(b, 4))
    print("abcd"[0])
